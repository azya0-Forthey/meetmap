from venv import logger
from typing import Callable

from pydantic import BaseModel
from sqlalchemy import select, ColumnElement, insert, update, exists, func
from sqlalchemy.exc import IntegrityError, DatabaseError
from sqlalchemy.orm import Mapped
from geoalchemy2.shape import to_shape

from database.models.placemark import PlaceMarkORM
from schemas.placemark import PlaceMarkBase, PlaceMarkDTO
from database.database import Base
from database.engine import async_session_factory


class Queries:
    @staticmethod
    async def select(orm: type[Base], schema: type[BaseModel], *where: ColumnElement[bool]) -> list[BaseModel]:
        async with async_session_factory() as session:
            query = (
                select(orm)
                .where(*where)
            )

            try:
                result = (await session.execute(query)).scalars().all()
            except DatabaseError as e:
                logger.warning(f"Error during database 'select': {e.args[1:]}")
                return []

            return [schema.model_validate(_, from_attributes=True) for _ in result]

    @staticmethod
    async def select_with_function(orm: type[Base], schema: type[BaseModel], function: Callable[[Base], Base], *where: ColumnElement[bool]) -> list[BaseModel]:
        async with async_session_factory() as session:
            query = (
                select(orm)
                .where(*where)
            )

            try:
                result = (await session.execute(query)).scalars().all()
            except DatabaseError as e:
                logger.warning(f"Error during database 'select': {e.args[1:]}")
                return []

            return [schema.model_validate(function(obj), from_attributes=True) for obj in result]

    @staticmethod
    async def select_one(orm: type[Base], schema: type[BaseModel], *where: ColumnElement[bool]) -> BaseModel | None:
        result = await Queries.select(orm, schema, *where)
        return result[0] if len(result) == 1 else None

    @staticmethod
    async def insert[ReturnType](
        table: type[Base], return_column: Mapped | None = None, **data
        ) -> ReturnType | None:

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
                logger.warning(f"Error during database 'insert': {e.args}")
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
                logger.warning(f"Error during database 'update': {e.args[1:]}")
                return False

    @staticmethod
    async def exists(table: type[Base], *where: ColumnElement[bool]) -> bool:
        async with async_session_factory() as session:
            query = (
                select(exists())
                .select_from(table)
                .where(*where)
            )

            try:
                result = (await session.execute(query)).scalar_one()

                await session.commit()
                return result
            except DatabaseError as e:
                logger.warning(f"Error during database 'exists': {e.args[1:]}")
                return False
    
    @staticmethod
    async def closest(mark: PlaceMarkBase, radius: float) -> list[PlaceMarkDTO]:
        """
        :param: radius Радиус в метрах
        """
        point = func.ST_GeomFromText(f'SRID=4326;POINT({mark.longitude} {mark.latitude})')

        query = select(PlaceMarkORM).where(func.ST_DistanceSphere(
            PlaceMarkORM.position, point
        ) <= radius)

        async with async_session_factory() as session:
            try:
                pre_result = (await session.execute(query)).scalars().all()

            except DatabaseError as error:
                logger.warning(f"Error during database 'closest': {error}")
        
        result = []

        for obj in pre_result:
            coords = to_shape(obj.position)

            obj.latitude = coords.x
            obj.longitude = coords.y

            result.append(PlaceMarkDTO.model_validate(obj, from_attributes=True))
        
        return result
