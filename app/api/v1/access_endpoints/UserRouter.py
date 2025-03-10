from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
import uuid

from app.schemas.User.UserSchema import UserSchema, UserRequestSchema, AccessSchema, TokenDecode
from app.configs import constants
from app.security.utils import decode_token,create_token
from app.services.User.UserService import UserService

UserRouter = APIRouter(prefix="/v1/travel_module", tags=["travel_module"])

@UserRouter.get("/", response_model=List[UserSchema])
def index(
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    userService: UserService = Depends(),
):
    return userService.list(pageSize=pageSize, startIndex=startIndex)

@UserRouter.get("/{id}", response_model=UserSchema)
def get(id: uuid.UUID, userService: UserService = Depends()):
    return userService.get(id)

@UserRouter.post("/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def create(user: UserRequestSchema, userService: UserService = Depends()):
    return userService.create(user)

@UserRouter.patch("/{id}", response_model=UserSchema)
def update(id: uuid.UUID, user: UserRequestSchema, userService: UserService = Depends()):
    return userService.update(id, user)

@UserRouter.delete("/{id}", response_model=dict)
def delete(id: uuid.UUID, userService: UserService = Depends()):
    userService.delete(id)
    return {"message": constants.DATA_DELETED}

@UserRouter.post("/login", response_model=dict)
def login(token: TokenDecode, userService: UserService = Depends()):
    token_dict = token.model_dump()
    
    try:
        data = decode_token(token_dict["token"])  # Decode token
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid token: {str(e)}")
 

    # Extract user details (optional, if needed for authentication)
    access_data = AccessSchema(
        signupid=data.get("signupid"),
        employeecode=data.get("employeecode"),
        subscriptionname=data.get("subscriptionname"),
        email=data.get("email"),
        employeeid=data.get("employeeid"),
    )

    userschema = userService.authenticate_user(accessSchema=access_data)
    if userschema is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    payload= userschema.model_dump()
    token=create_token(payload)
    return {"Travel Module Access Token":token}


