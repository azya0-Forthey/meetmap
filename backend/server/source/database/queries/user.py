from database.models.user import UserORM
from database.queries import orm
from schemas.user import UserAddDTO


async def register_user(user: UserAddDTO) -> int:
    return await orm.Queries.insert(UserORM, UserORM.id, **user.model_dump())
