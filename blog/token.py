from datetime import datetime, timedelta
from typing import Optional
import jwt
from . import schemas

from jose import JWTError,jwt


SECRET_KEY = "your_secret_key_here"
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
    to_encode = data.copy()

    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expires})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY, algorithm =ALGORITHM)
    return encoded_jwt   

def verify_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
         raise credentials_exception
   