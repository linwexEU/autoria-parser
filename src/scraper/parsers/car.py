import logging
from typing import Optional

from playwright.async_api import Page

from src.scraper.utils.retry import retry
from src.schemas.car import CarDTO
from src.scraper.browser.context import Context
from src.utils.logger import configure_logging 

logger = logging.getLogger(__name__)
configure_logging()


class ParseCar: 
    def __init__(self) -> None: 
        self._context = None

    async def init_context(self) -> None: 
        self._context = Context() 
        await self._context.init_playwright()

    @property
    def page(self) -> Page: 
        return self._context._page 
    
    async def get_title(self) -> Optional[str]: 
        try:
            title = self.page.locator("//div[@id='sideTitleTitle']/span[@class='common-text ws-pre-wrap titleM']")
            logging.info("Get car title.")
            return await title.text_content()
        except Exception as exc: 
            logger.error(str(exc))

    async def get_price_usd(self) -> Optional[str]: 
        try:
            price_usd = self.page.locator("//div[@id='sidePrice']/strong[@class='common-text ws-pre-wrap titleL']")
            logging.info("Get car price.")
            return await price_usd.text_content()
        except Exception as exc: 
            logger.error(str(exc))

    async def get_odometer(self) -> Optional[str]: 
        try:
            odometer = self.page.locator("//div[@id='basicInfoTableMainInfo0']/span[@class='common-text ws-pre-wrap body']")
            logging.info("Get car odometer.")
            return await odometer.text_content()
        except Exception as exc: 
            logger.error(str(exc))

    async def get_username(self) -> Optional[str]: 
        try:
            username = self.page.locator("//div[@id='sellerInfoUserName']/span[@class='common-text ws-pre-wrap titleM']")
            logging.info("Get car owner.")
            return await username.text_content()
        except Exception as exc: 
            logger.error(str(exc))

    async def get_image_url(self) -> Optional[str]: 
        try:
            image_url = self.page.locator("//span[@class='picture']//img")
            logging.info("Get car image url.")
            return await image_url.nth(0).get_attribute("src")
        except Exception as exc: 
            logger.error(str(exc))

    async def get_images_count(self) -> Optional[str]: 
        try:
            images_count = self.page.locator("//span[@class='common-badge alpha medium']")
            logging.info("Get car images count.")
            return await images_count.nth(0).text_content()
        except Exception as exc: 
            logger.error(str(exc))

    async def get_car_number(self) -> Optional[str]: 
        try:
            car_number = self.page.locator("//div[@class='car-number ua']/span")
            logging.info("Get car number.")
            return await car_number.text_content()
        except Exception as exc: 
            logger.error(str(exc))

    async def get_car_vin(self) -> Optional[str]: 
        try:
            car_vin = self.page.locator("//div[@id='badgesVinGrid']/div/span/span")
            logging.info("Get car vin.")
            return await car_vin.text_content()
        except Exception as exc: 
            logger.error(str(exc))

    async def get_phone_number(self) -> Optional[str]: 
        try:
            get_phone_button = self.page.locator("//div[@class='button-main mt-12']/button[@class='size-large conversion']")
            await get_phone_button.nth(0).click()
            
            phone_number = self.page.locator("//div[@id='autoPhonePopUpResponse']//span[@class='common-text ws-pre-wrap action']")
            logging.info("Get owner's phone number.")
            return await phone_number.nth(0).text_content()
        except Exception as exc: 
            logger.error(str(exc))
    
    @retry()
    async def collect_car(self, link: str) -> CarDTO: 
        await self.page.goto(link) 
        logger.info(f"Go to {link}.")

        title = await self.get_title() 
        price_usd = await self.get_price_usd() 
        odometer = await self.get_odometer() 
        username = await self.get_username() 
        image_url = await self.get_image_url() 
        images_count = await self.get_images_count()
        car_number = await self.get_car_number() 
        car_vin = await self.get_car_vin()
        phone_number = await self.get_phone_number()

        return CarDTO(link, title, price_usd, odometer, username, 
                      phone_number, image_url, images_count, 
                      car_number, car_vin)

    async def close_page(self) -> None: 
        await self._context._page.close()

    async def new_page(self) -> None: 
        await self._context.new_page()

    async def close_context(self) -> None: 
        await self._context.close_context()
