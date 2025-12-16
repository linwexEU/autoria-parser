from typing import Any

from src.db.base import async_session_maker
from src.repositories.car import CarRepostiry


class UnitOfWork: 
    car_repository: CarRepostiry = None 

    def __init__(self) -> None: 
        self.session = async_session_maker()

    async def commit(self) -> None: 
        await self.session.commit() 

    async def rollback(self) -> None: 
        await self.session.rollback()

    async def __aenter__(self) -> "UnitOfWork":
        self.car_repository = CarRepostiry(self.session)
        return self
    
    async def __aexit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: 
        if exc_type is None: 
            await self.commit()
        else: 
            await self.rollback() 
        await self.session.close()
