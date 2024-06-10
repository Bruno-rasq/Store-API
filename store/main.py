from fastapi import FastAPI
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