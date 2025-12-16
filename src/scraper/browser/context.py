from typing import Optional

from playwright.async_api import async_playwright, Playwright, Browser, Page


class Context: 
    def __init__(self) -> None:
        self._playwright: Optional[Playwright] = None
        self._browser: Optional[Browser] = None
        self._page: Optional[Page] = None

    async def init_playwright(self) -> None:
        self._playwright = await async_playwright().start()
        self._browser = await self._playwright.firefox.launch(headless=True)
        self._page = await self._browser.new_page()

        # Settings
        self._page.set_default_timeout(5000)

    async def new_page(self) -> None: 
        self._page = await self._browser.new_page()

        # Settings
        self._page.set_default_timeout(5000)

    async def close_context(self) -> None: 
        if self._page:
            await self._page.close() 

        if self._browser:
            await self._browser.close() 
        
        if self._playwright:
            await self._playwright.stop()
