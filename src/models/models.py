from datetime import datetime

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column 

from src.db.base import Base


class Car(Base): 
    __tablename__ = "car"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(unique=True)
    title: Mapped[str] = mapped_column() 
    price_usd: Mapped[int] = mapped_column()
    odometer: Mapped[int] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column()
    phone_number: Mapped[int] = mapped_column(BigInteger, nullable=True)
    image_url: Mapped[str] = mapped_column(nullable=True) 
    images_count: Mapped[int] = mapped_column(nullable=True)
    car_number: Mapped[str] = mapped_column(nullable=True) 
    car_vin: Mapped[str] = mapped_column(nullable=True)
    datetime_found: Mapped[datetime] = mapped_column(default=datetime.now())
