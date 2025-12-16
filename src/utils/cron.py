from apscheduler.triggers.cron import CronTrigger

from src.config import settings


def build_parser_daily_cron() -> None: 
    hour, minute = settings.SCRAPER_RUN_TIME.split(":") 
    return CronTrigger(hour=hour - 2, minute=minute)


def build_dump_daily_cron() -> None: 
    hour, minute = settings.DUMP_RUN_TIME.split(":") 
    return CronTrigger(hour=hour - 2, minute=minute)
