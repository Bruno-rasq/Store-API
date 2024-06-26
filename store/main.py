import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from store.db.db_create import create_db
from store.db.db_client import db_client
from store.controllers.api_router import router
from store.core.config import settings


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
          *args,
          **kwargs,
          title=settings.PROJECT_NAME,
          # root_path=settings.ROOT_PATH
        )


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db(db_client)
    yield


# app = App()
app = App(lifespan=lifespan)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)