from .base import Base
from sqlalchemy.orm import Mapped


class Product(Base):
    __tablename__ = "products"

    name: Mapped[str]
    discription: Mapped[str]
    price: Mapped[int]
