from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException
import jwt
import uuid

SECRET_KEY = "WdiXZinghr@2025"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")




def decode_token(token: str):
    print("token: ", token)
    decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    print("decoded_payload: ", decoded_payload)
    return decoded_payload


def create_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = {k: str(v) if isinstance(v, uuid.UUID) else v for k, v in data.items()}
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

