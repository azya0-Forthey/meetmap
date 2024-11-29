from pydantic import BaseModel

class UserLoginDTO(BaseModel):
    username: str
    password: str

class UserAddDTO(UserLoginDTO):
    email: str

class UserDTO(UserAddDTO):
    id: int

class UserSecureDTO(BaseModel):
    id: int
    username: str
    email: str
