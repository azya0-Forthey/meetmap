from database.models.placemark import PlaceMarkORM
from database.queries import orm
from schemas.placemark import PlaceMarkDTO, PlaceMarkAddDTO


async def get_user_placemarks(user_id: int) -> list[PlaceMarkDTO]:
    return await orm.get(PlaceMarkORM, PlaceMarkDTO, PlaceMarkORM.create_user_id == user_id)


async def add_placemark(placemark: PlaceMarkAddDTO) -> int:
    return await orm.add(PlaceMarkORM, PlaceMarkORM.id, **placemark.model_dump())