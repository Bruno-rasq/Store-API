from store.schemas.base import BaseSchemaMixin
from pydantic import Field

class ProductIn(BaseSchemaMixin):
  name:     str   = Field(..., description= "product name")
  quantity: int   = Field(..., description= "product qunatity")
  price:    float = Field(..., description= "product price")
  status:   bool  = Field(..., description= "product status")
  