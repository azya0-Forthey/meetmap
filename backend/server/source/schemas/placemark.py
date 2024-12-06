from datetime import datetime

from pydantic import BaseModel


class PlaceMarkBase(BaseModel):
    latitude: float
    longitude: float


class PlaceMarkAddDTO(PlaceMarkBase):
    name: str
    description: str | None
    latitude: float
    longitude: float


class PlaceMarkDTO(PlaceMarkAddDTO):
    id: int
    create_date: datetime
    is_active: bool
    user_id: int