from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base, IntPrimKey, CreateDate


class PlaceMarkORM(Base):
    __tablename__ = "placemarks"

    id: Mapped[IntPrimKey]

    name: Mapped[str]
    description: Mapped[str]
    latitude: Mapped[float]
    longitude: Mapped[float]
    create_date: Mapped[CreateDate]
    is_active: Mapped[bool] = mapped_column(default=True, server_default="true")

    create_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))