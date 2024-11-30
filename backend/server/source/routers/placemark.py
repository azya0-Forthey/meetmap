from fastapi import APIRouter, HTTPException
from starlette import status

import database.queries.placemarks as placemarks_db
from auth.auth import AuthUser
from schemas.placemark import PlaceMarkDTO, PlaceMarkAddDTO

router = APIRouter(
    prefix="/placemarks",
    tags=["placemarks"],
)

@router.get("/")
async def get_placemarks(user: AuthUser) -> list[PlaceMarkDTO]:
    return await placemarks_db.get_user_placemarks(user.id)

@router.post("/")
async def create_placemark(user: AuthUser, placemark: PlaceMarkAddDTO) -> int:
    # TODO verify user validity (after auth)
    placemark_id = await placemarks_db.add_placemark(user.id, placemark)
    if not placemark_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return placemark_id


@router.delete("/")
async def close_placemark(user: AuthUser, placemark_id: int) -> int:
    placemark_id = await placemarks_db.close_placemark(user.id, placemark_id)
    if not placemark_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return placemark_id