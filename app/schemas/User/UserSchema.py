from pydantic import BaseModel
import uuid


class UserRequestSchema(BaseModel):
    signupid:int
    subscriptionname:str
    employeecode:str
    firstName:str
    lastName:str
    email:str
    name:str
    photo:str
    employeeid:int


class UserSchema(UserRequestSchema):
    id: uuid.UUID

class TokenDecode(BaseModel):
    token: str

class AccessSchema(BaseModel):
    signupid:int
    employeecode:str
    subscriptionname:str
    email:str
    employeeid:int


