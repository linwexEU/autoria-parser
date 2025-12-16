import os

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings

current_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(current_dir)

dotenv_path = find_dotenv(".env")
load_dotenv(dotenv_path)


class Settings(BaseSettings): 
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_PASS: str
    DB_USER: str

    SCRAPER_RUN_TIME: str
    DUMP_RUN_TIME: str

    BACKUP_DIR: str

    @property
    def DATABASE_URL(self) -> str: 
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}" 
    
    class ConfigDict:
        env_file = dotenv_path


settings = Settings() 
