from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    def __repr__(self):
        columns = []
        for column in self.__table__.columns.keys():
            columns.append(f"{column}={getattr(self, column)}")

        return f"[{self.__class__.__name__}]\n\t {",\n\t".join(columns)}"
