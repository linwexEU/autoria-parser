import subprocess
import os
from datetime import datetime
import logging

from src.config import settings
from src.utils.logger import configure_logging

logger = logging.getLogger(__name__)
configure_logging()


async def task_create_backup() -> None: 
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(settings.BACKUP_DIR, f"{settings.DB_NAME}_{timestamp}.sql")

    command = [
        "pg_dump", 
        "-h", settings.DB_HOST, 
        "-p", str(settings.DB_PORT), 
        "-U", settings.DB_USER, 
        "-F", "c", 
        "-f", backup_file, 
        settings.DB_NAME
    ]
    env = os.environ.copy()
    env["PGPASSWORD"] = settings.DB_PASS

    res = subprocess.run(command, env=env)
    if res.returncode == 0: 
        logger.info(f"Backup created successfully: {backup_file}")
    else: 
        logger.error("Backup failed")
