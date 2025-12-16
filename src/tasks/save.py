import logging

from sqlalchemy.exc import IntegrityError

from src.scraper.parsers.car import ParseCar
from src.utils.unit_of_work import UnitOfWork
from src.utils.logger import configure_logging

logger = logging.getLogger(__name__)
configure_logging()


async def task_save_car_to_db(parser: ParseCar, link: str) -> None: 
    async with UnitOfWork() as uow: 
        car = await uow.car_repository.get_by_url(link)
        if car: 
            logger.warning(f"{link} has been already parsed.")
            return 
        
        car_dto = await parser.collect_car(link)
        if car_dto is not None:
            try:
                await uow.car_repository.insert(car_dto.to_dict())
            except IntegrityError as exc:
                logger.error(str(exc))
