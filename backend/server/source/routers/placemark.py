from fastapi import APIRouter, HTTPException
from starlette import status

import database.queries.placemarks as placemarks_db
from auth.user_service import AuthUser
from schemas.placemark import PlaceMarkBase, PlaceMarkDTO, PlaceMarkAddDTO

router = APIRouter(
    prefix="/placemarks",
    tags=["placemarks"],
)

@router.get("/")
async def get_placemarks(user: AuthUser) -> list[PlaceMarkDTO]:
    return await placemarks_db.get_user_placemarks(user.id)

@router.post("/")
async def create_placemark(user: AuthUser, placemark: PlaceMarkAddDTO) -> int:
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


@router.post("/closests")
async def closest_placemarks(user: AuthUser, mark: PlaceMarkBase, radius: float) -> list[PlaceMarkAddDTO]:
    return await placemarks_db.closest_placemarks(mark, radius)
