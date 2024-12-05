from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from geoalchemy2 import Geometry

from database.database import Base, IntPrimKey, CreateDate


class PlaceMarkORM(Base):
    __tablename__ = "placemarks"

    id: Mapped[IntPrimKey]

    name: Mapped[str]
    description: Mapped[str]
    position: Mapped[Geometry] = mapped_column(Geometry(geometry_type='POINT', srid=4326))
    
    create_date: Mapped[CreateDate]
    is_active: Mapped[bool] = mapped_column(default=True, server_default="true")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
