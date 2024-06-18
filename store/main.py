import uvicorn
from fastapi import FastAPI
from store.db.db_create import create_db
from store.db.db_client import db_client
from store.controllers.api_router import router
from store.core.config import settings


class App(FastAPI):
  def __ini__(self, *args, **kwargs) -> None:
    super().__init__(
      *args,
      **kwargs,
      title= settings.PROJECT_NAME,
      root_path= settings.ROOT_PATH
    )

app = App()
app.include_router(router)


@app.on_event("startup")
def setup_db():
  create_db(db_client)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8080)