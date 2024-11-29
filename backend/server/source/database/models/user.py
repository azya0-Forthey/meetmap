from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from database.database import IntPrimKey, Base


class UserORM(Base):
    __tablename__ = 'users'

    id: Mapped[IntPrimKey]
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
    password: Mapped[str]