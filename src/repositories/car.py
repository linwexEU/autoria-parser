from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from src.models.models import Car


class CarRepostiry: 
    def __init__(self, session: AsyncSession) -> None: 
        self._session = session 

    async def insert(self, payload: dict) -> int: 
        query = insert(Car).values(**payload).returning(Car.id)
        res = await self._session.execute(query)
        return res.scalar() 

    async def get_by_url(self, url: str) -> Optional[Car]: 
        query = select(Car).where(Car.url == url)
        res = await self._session.execute(query)
        return res.scalar_one_or_none()
