from auth import hashing
from database.models.user import UserORM
from database.queries import orm
from schemas.user import UserAddDTO, UserDTO


async def register_user(user: UserAddDTO) -> int | None:
    user.password = hashing.hash_pwd(user.password)
    return await orm.Queries.insert(UserORM, UserORM.id, **user.model_dump())

async def get_user(username: str) -> UserDTO | None:
    return await orm.Queries.select_one(UserORM, UserDTO, UserORM.username == username)