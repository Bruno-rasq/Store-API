from store.schemas.base import BaseSchemaMixin
from pydantic import Field, BaseModel

class ProductIN(BaseModel):
  name        : str   = Field(..., description="product name")
  description : str   = Field(..., description="product description")
  price       : float = Field(..., description="product price")
  quantity    : int   = Field(..., description="product quantity")

class ProductOUT(BaseSchemaMixin, ProductIN):
  pass