from sqlalchemy.orm import Mapped

from database.database import IntPrimKey, Base


class UserORM(Base):
    __tablename__ = 'users'

    id: Mapped[IntPrimKey]
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]