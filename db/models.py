from flask_login import UserMixin

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import String, Integer, DATE, Double, ForeignKey, Text
from typing import Optional
from db.db import engine



class Base(DeclarativeBase):
    pass
# db için user table oluşturulur


class User(UserMixin, Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(Text(), unique=True)
    password: Mapped[Optional[str]]


Base.metadata.create_all(bind=engine)