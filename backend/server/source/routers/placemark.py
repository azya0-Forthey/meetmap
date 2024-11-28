from fastapi import APIRouter

import database.queries.placemarks as placemarks_db
from schemas.placemark import PlaceMarkDTO, PlaceMarkAddDTO

router = APIRouter(
    prefix="/placemarks",
    tags=["placemarks"],
)

@router.get("/", response_model=list[PlaceMarkDTO])
async def get_placemarks(user_id: int):
    return await placemarks_db.get_user_placemarks(user_id)

@router.post("/", response_model=int)
async def create_placemark(placemark: PlaceMarkAddDTO):
    # TODO verify user validity (after auth)
    return await placemarks_db.add_placemark(placemark)