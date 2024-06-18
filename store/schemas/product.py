from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ProductIN(BaseModel):
  name        : str   = Field(..., description="product name")
  description : str   = Field(..., description="product description")
  price       : float = Field(..., description="product price")
  quantity    : int   = Field(..., description="product quantity")



class ProductOUT(ProductIN, BaseModel):
  id         : Optional[int]      = Field(None, description="The unique identifier of the product")
  created_at : Optional[datetime] = Field(None, description="The timestamp when the product was created")
  updated_at : Optional[datetime] = Field(None, description="The timestamp when the product was last updated")