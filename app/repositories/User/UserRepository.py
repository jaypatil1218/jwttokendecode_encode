from typing import List, Optional
import uuid
from fastapi import Depends
from sqlalchemy.orm import Session
from app.configs.Database import get_db_connection
from app.models.User.UserModel import User
from app.schemas.User.UserSchema import AccessSchema
from app.repositories.BaseRepository import (
    BaseRepository,
)


class UserRepository(BaseRepository[User, uuid.UUID]):  
    def __init__(self, db: Session = Depends(get_db_connection)):
        super().__init__(db, User)
        

    def getByToken(self,accessSchema:AccessSchema):
    
        user = self.db.query(User).filter(User.signupid == accessSchema.signupid,
                                          User.email==accessSchema.email,
                                          User.employeecode==accessSchema.employeecode,
                                          User.subscriptionname==accessSchema.subscriptionname,
                                          User.employeeid==accessSchema.employeeid).first()
        return user
