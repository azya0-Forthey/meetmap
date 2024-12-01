from datetime import datetime

from pydantic import BaseModel


class PlaceMarkAddDTO(BaseModel):
    name: str
    description: str | None
    latitude: float
    longitude: float

class PlaceMarkDTO(PlaceMarkAddDTO):
    id: int
    create_date: datetime
    is_active: bool
    user_id: int