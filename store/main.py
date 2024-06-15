import uvicorn
from fastapi import FastAPI
from core.config import settings
from controllers.api_router import router
from db.setup_db import setup_database

class App(FastAPI):
  def __ini__(self, *args, **kwargs) -> None:
    super().__init__(
      *args,
      **kwargs,
      title= settings.PROJECT_NAME,
      root_path= settings.ROOT_PATH
    )

setup_database()
app = App()
app.include_router(router)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8080)