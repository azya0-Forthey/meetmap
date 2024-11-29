from venv import logger

from pydantic import BaseModel
from sqlalchemy import select, ColumnElement, insert, update
from sqlalchemy.exc import IntegrityError, DatabaseError
from sqlalchemy.orm import Mapped

from database.database import Base
from database.engine import async_session_factory


class Queries:
    @staticmethod
    async def select(orm: type(Base), schema: type(BaseModel), *where: ColumnElement[bool]) -> list[BaseModel]:
        async with async_session_factory() as session:
            query = (
                select(orm)
                .where(*where)
            )

            result = (await session.execute(query)).scalars().all()

            return [schema.model_validate(_, from_attributes=True) for _ in result]

    @staticmethod
    async def insert[ReturnType](table: type[Base], return_column: Mapped | None = None,
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

                await session.commit()
                return result
            except DatabaseError as e:
                logger.warning(f"error during database 'insert': {e.args[1:]}")
                return None

    @staticmethod
    async def update(table: type[Base], returning: Mapped | Base = Base, *where: ColumnElement[bool], **values) -> bool:
        async with async_session_factory() as session:
            query = (
                update(table)
                .where(*where)
                .values(**values)
                .returning(returning)
            )

            try:
                result = (await session.execute(query)).scalars().all()

                await session.commit()
                return len(result) != 0
            except DatabaseError as e:
                logger.warning(f"error during database 'update': {e.args[1:]}")
                return False
