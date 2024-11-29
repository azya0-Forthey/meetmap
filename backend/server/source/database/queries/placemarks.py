from database.models.placemark import PlaceMarkORM
from database.queries import orm
from schemas.placemark import PlaceMarkDTO, PlaceMarkAddDTO


async def get_user_placemarks(user_id: int) -> list[PlaceMarkDTO]:
    return await orm.Queries.select(PlaceMarkORM, PlaceMarkDTO, PlaceMarkORM.create_user_id == user_id)


async def add_placemark(placemark: PlaceMarkAddDTO) -> int:
    return await orm.Queries.insert(PlaceMarkORM, PlaceMarkORM.id, **placemark.model_dump())


async def change_placemark_state(placemark_id: int, is_active: bool) -> int | None:
    return await orm.Queries.update(PlaceMarkORM, PlaceMarkORM.id, PlaceMarkORM.id == placemark_id,
                                    is_active=is_active)

async def close_placemark(place_mark_id: int) -> int | None:
    return await change_placemark_state(place_mark_id, False)