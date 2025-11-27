from fastapi import HTTPException,status
from tortoise.exceptions import DoesNotExist
from models.user import User
from auth.hashing import hash_password,verify_password
from auth.token import create_access_token,create_refresh_token,decode_token

class AuthService:

    async def register_user(self,username:str,email:str,password:str):
        exists = await User.get_or_none(email=email)

        if exists:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Email already in use")
        
        hashed_password = hash_password(password)

        user = await User.create(username=username,email=email,password=hashed_password)

        return user
    
    async def login_user(self,email:str,password:str):
        user = await User.get_or_none(email=email)

        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid email address")
        
        if not verify_password(user.password,password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid password")
        
        access_token = create_access_token({"user_id":user.id})
        refresh_token = create_refresh_token({"user_id":user.id})

        return {
            "access_token":access_token,
            "refresh_token":refresh_token,
            "token_type":"bearer"
        }
    
    async def get_current_user(self,token:str):
        payload = decode_token(token)

        if not payload:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid or expired token")
        
        user_id = payload["user_id"]

        try:
            user = await User.get(id=user_id)
            return user
        except DoesNotExist:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User not found")


auth_service = AuthService()