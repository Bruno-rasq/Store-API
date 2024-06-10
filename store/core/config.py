from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
  PROJECT_NAME: str = "Store API"
  ROOT_PATH:    str = "/"
  DATABASE_URL: str =  ''
  DATABASE_PATH: Path = Path('/store/db/Products.db')

settings = Settings()