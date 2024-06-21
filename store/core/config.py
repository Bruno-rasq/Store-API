from pydantic_settings import BaseSettings


class Settings(BaseSettings):
  PROJECT_NAME: str = "Store API"
  # ROOT_PATH:    str = "/"
  

settings = Settings()