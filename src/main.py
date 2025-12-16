import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.tasks.parser import task_run_parser
from src.tasks.backup import task_create_backup
from src.utils.logger import configure_logging
from src.utils.cron import build_dump_daily_cron, build_parser_daily_cron

logger = logging.getLogger(__name__)
configure_logging() 


async def main() -> None: 
    scheduler = AsyncIOScheduler()

    scheduler.add_job(task_run_parser, build_dump_daily_cron())
    scheduler.add_job(task_create_backup, build_parser_daily_cron())

    scheduler.start()
    logger.info("Scheduler started")

    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__": 
    asyncio.run(main())
