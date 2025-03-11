from typing import List, Optional
from fastapi import Depends
from app.models.User.UserModel import User
from app.repositories.User.UserRepository import UserRepository
from app.schemas.User.UserSchema import UserRequestSchema,AccessSchema
import uuid




class UserService:
    userRepository: UserRepository

    def __init__(self, userRepository: UserRepository = Depends()) -> None:
        self.userRepository = userRepository

    def create(self, user_body: UserRequestSchema) -> User:

        user_instance=User(
            **user_body.model_dump()
        )
        return self.userRepository.create(instance=user_instance)

    def delete(self, user_id: int) -> None:
        return self.userRepository.delete(user_id)

    def get(self, user_id: int) -> User:
        return self.userRepository.get(user_id)

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[User]:
        return self.userRepository.list( pageSize, startIndex)

    def update(self, user_id: int, emp_body: UserRequestSchema) -> User:
        return self.userRepository.update(user_id, emp_body)
    
    def authenticate_user(self, accessSchema:AccessSchema) -> UserRequestSchema:
        user=self.userRepository.getByToken(accessSchema)
        if user is None:
            return None  # Or raise an exception if you want

        return UserRequestSchema(**user.__dict__)  




 