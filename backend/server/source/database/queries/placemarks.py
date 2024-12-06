from sqlalchemy import and_

from database.models.placemark import PlaceMarkORM
from database.queries import orm
from schemas.placemark import PlaceMarkDTO, PlaceMarkAddDTO
from geoalchemy2.shape import to_shape


async def get_user_placemarks(user_id: int) -> list[PlaceMarkDTO]:
    def reform(value: PlaceMarkORM) -> PlaceMarkORM:
        coords = to_shape(value.position)

        value.latitude = coords.x
        value.longitude = coords.y

        return value
            
    return await orm.Queries.select_with_function(PlaceMarkORM, PlaceMarkDTO, reform, PlaceMarkORM.user_id == user_id)


async def add_placemark(user_id: int, placemark: PlaceMarkAddDTO) -> int | None:
    dumped_model = placemark.model_dump()
    dumped_model['position'] = f'SRID=4326;POINT({dumped_model.pop("latitude")} {dumped_model.pop("longitude")})'

    return await orm.Queries.insert(PlaceMarkORM, PlaceMarkORM.id, user_id=user_id, **dumped_model)


async def change_placemark_state(user_id: int, placemark_id: int, is_active: bool) -> int | None:
    return await orm.Queries.update(PlaceMarkORM, PlaceMarkORM.id,
                                    and_(PlaceMarkORM.id == placemark_id, PlaceMarkORM.user_id == user_id),
                                    is_active=is_active)


async def close_placemark(user_id: int, place_mark_id: int) -> int | None:
    return await change_placemark_state(user_id, place_mark_id, False)
