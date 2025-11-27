from fastapi import APIRouter,Depends,status
from fastapi.security import OAuth2PasswordBearer
from schemas.auth_schemas import RegisterSchema,LoginScheme,UserOut,TokenSchema
from auth.auth_service import auth_service
from models.user import User

router = APIRouter(prefix="/api/auth", tags=["Authentication"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

@router.post("/register",response_model=UserOut,status_code=status.HTTP_201_CREATED)
async def register_user(payload:RegisterSchema):
    user = await auth_service.register_user(
        username=payload.username,
        email=payload.email,
        password=payload.password
    )

    return user


@router.post("/login",response_model=TokenSchema,status_code=status.HTTP_200_OK)
async def login_user(payload:LoginScheme):
    tokens =  await auth_service.login_user(
        email=payload.email,
        password=payload.password
    )

    return tokens


# Dependency to get current user logged in
async def get_current_user(token:str = Depends(oauth2_scheme)) -> User:
    user = await auth_service.get_current_user(token)
    return user

# protected route
@router.get("/me",response_model=UserOut,status_code=status.HTTP_200_OK)
async def read_current_user(current_user:User = Depends(get_current_user)):
    return current_user