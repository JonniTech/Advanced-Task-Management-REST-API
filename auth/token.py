from datetime import datetime,timedelta
import jwt
from configs.settings import SECRET_KEY,REFRESH_TOKEN_EXPIRE_DAYS,ACCESS_TOKEN_EXPIRE_MINUTES

ALGORITHM = "HS256"

def create_access_token(data:dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

def create_refresh_token(data:dict):
    payload =  data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)

    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

def decode_token(token:str) -> dict | None:
    try:
        return jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None