from fastapi import APIRouter, HTTPException, status
from typing import List

# DB - metodos
from store.db.db_client import db_client

from store.db.db_products import (
delete_product_db,
get_all_products_db,
get_product_by_id_db,
  insert_product__db,
  update_product_db,
) 

# models 
from store.schemas.product import ProductIN, ProductOUT 


router = APIRouter()


@router.get("/")
async def root_path():
  return {"message": "ok"}


@router.get("/products", tags=["products"], response_model=List[ProductOUT])
async def pegar_produtos():
  return get_all_products_db(db_client)


@router.get("/products/{id}", tags=["products"], response_model=ProductOUT)
async def pegar_produto_id(id: int):
  product = get_product_by_id_db(db_client, id)
  if product is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
  return product


@router.post('/products', response_model=ProductOUT, tags=["products"])
async def cadastrar_produto(produto: ProductIN):
  novo_produto = insert_product__db(db_client, produto.name, produto.description, produto.price, produto.quantity)
  return novo_produto


@router.put("/products/{id}", tags=["products"], response_model=ProductOUT)
async def update_produto(id: int, prod: ProductIN):
  return update_product_db(db_client, id, prod.name, prod.description, prod.price, prod.quantity)


@router.delete("/products/{id}", tags=["products"], status_code=status.HTTP_204_NO_CONTENT)
async def deletar_produto(id: int):
  sucess = delete_product_db(db_client, id)
  if not sucess:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="product not found")
  return None
  