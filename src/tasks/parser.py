from src.scraper.parsers.car import ParseCar
from src.scraper.parsers.listing import ParseListing
from src.tasks.save import task_save_car_to_db


async def task_run_parser() -> None: 
    # Init parsers
    parser_car = ParseCar()
    parser_listing = ParseListing()

    # Init context
    await parser_car.init_context()
    await parser_listing.init_context()

    page_count = 0
    while True:
        url = f"https://auto.ria.com/uk/search/?indexName=auto&page={page_count}"
        links: list[str] = await parser_listing.collect_listings(url)
        
        if links is None: 
            page_count += 1
            continue

        if len(links) == 0: # page doesn't exist
            break 

        for link in links: 
            await task_save_car_to_db(parser_car, link)
            
        page_count += 1
        await parser_car.close_page()
        await parser_car.new_page()

    await parser_car.close_context()
    await parser_listing.close_context()
