from dataclasses import dataclass, asdict
from typing import Optional


@dataclass(slots=True)
class CarDTO: 
    url: Optional[str] = None
    title: Optional[str] = None
    price_usd: Optional[int] = None
    odometer: Optional[int] = None
    username: Optional[str] = None
    phone_number: Optional[int] = None
    image_url: Optional[str] = None
    images_count: Optional[int] = None
    car_number: Optional[str] = None
    car_vin: Optional[str] = None

    def __post_init__(self) -> None: 
        if self.price_usd is not None:
            self.price_usd = int(self.price_usd.replace("$", "").replace("\xa0", ""))

        if self.username is not None:
            self.username = self.username.strip()

        if self.odometer is not None: 
            self.odometer = int(self.odometer.split(" ")[0]) * 1000

        if self.images_count is not None:
            self.images_count = int(self.images_count.split(" ")[-1].strip())

        if self.phone_number is not None:
            self.phone_number = int("38" + self.phone_number.replace("(", "").replace(")", "").replace(" ", ""))

    def to_dict(self) -> dict: 
        return asdict(self)
