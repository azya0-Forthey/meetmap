from pydantic import BaseModel
from sqlalchemy import select, ColumnElement, insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Mapped

from database.database import Base
from database.engine import async_session_factory


async def get(orm: type(Base), schema: type(BaseModel), *where: ColumnElement[bool]) -> list[BaseModel]:
    async with async_session_factory() as session:
        query = (
            select(orm)
            .where(*where)
        )

        result = (await session.execute(query)).scalars().all()

        return [schema.model_validate(_, from_attributes=True) for _ in result]

async def add[ReturnType](table: type[Base], return_column: Mapped | None = None,
                                 **data) -> ReturnType | None:
    async with async_session_factory() as session:
        query = (
            insert(table)
            .values(**data)
        )
        if return_column:
            query = query.returning(return_column)

        try:
            result = (await session.execute(query)).scalar_one_or_none()
        except IntegrityError:
            return None

        await session.commit()
        return result
