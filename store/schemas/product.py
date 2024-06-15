from store.schemas.base import BaseSchemaMixin
from pydantic import Field, BaseModel

class ProductIn(BaseModel):
  name:     str   = Field(..., description= "product name")
  quantity: int   = Field(..., description= "product qunatity")
  price:    float = Field(..., description= "product price")
  status:   bool  = Field(..., description= "product status")

class ProductOUT(BaseSchemaMixin):
  name:     str   = Field(..., description= "product name")
  quantity: int   = Field(..., description= "product qunatity")
  price:    float = Field(..., description= "product price")
  status:   bool  = Field(..., description= "product status")