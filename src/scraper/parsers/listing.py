import logging

from playwright.async_api import Page, Locator

from src.scraper.utils.retry import retry
from src.scraper.browser.context import Context
from src.utils.logger import configure_logging

logger = logging.getLogger(__name__)
configure_logging()


class ParseListing:
    def __init__(self) -> None: 
        self._context = None

    @property
    def page(self) -> Page: 
        return self._context._page

    async def init_context(self) -> None: 
        self._context = Context()
        await self._context.init_playwright()

    @retry()
    async def collect_listings(self, url: str) -> list[str]:
        await self.page.goto(url)
        logger.info(f"Go to {url}.")
        
        links: list[Locator] = self.page.locator("//a[@class='link product-card horizontal']")
        count = await links.count()

        if count == 0: 
            return []
        
        urls = []
        for i in range(count): 
            href = await links.nth(i).get_attribute("href")
            link = "https://auto.ria.com" + href
            urls.append(link)

        logger.info(f"Parsed all links({count}) from {url}.")
        return urls 
    
    async def close_context(self) -> None: 
        await self._context.close_context()
