from pydantic import BaseModel


class UserAddDTO(BaseModel):
    username: str
    email: str
    password: str


class UserDTO(UserAddDTO):
    id: int
