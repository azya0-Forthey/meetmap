from sqlalchemy import and_

from database.models.placemark import PlaceMarkORM
from database.queries import orm
from schemas.placemark import PlaceMarkDTO, PlaceMarkAddDTO


async def get_user_placemarks(user_id: int) -> list[PlaceMarkDTO]:
    return await orm.Queries.select(PlaceMarkORM, PlaceMarkDTO, PlaceMarkORM.user_id == user_id)


async def add_placemark(user_id: int, placemark: PlaceMarkAddDTO) -> int | None:
    return await orm.Queries.insert(PlaceMarkORM, PlaceMarkORM.id, user_id=user_id, **placemark.model_dump())


async def change_placemark_state(user_id: int, placemark_id: int, is_active: bool) -> int | None:
    return await orm.Queries.update(PlaceMarkORM, PlaceMarkORM.id,
                                    and_(PlaceMarkORM.id == placemark_id, PlaceMarkORM.user_id == user_id),
                                    is_active=is_active)


async def close_placemark(user_id: int, place_mark_id: int) -> int | None:
    return await change_placemark_state(user_id, place_mark_id, False)
