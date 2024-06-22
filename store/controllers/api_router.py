from fastapi import APIRouter, HTTPException, status
from store.schemas.product import ProductIN, ProductOUT, ProductsDB
from store.db.db_client import db_client
from store.db.db_products import (
  delete_product_db,
  get_all_products_db,
  get_product_by_id_db,
  insert_product__db,
  update_product_db,
) 


router = APIRouter()


@router.get("/")
def root_path():
  return {"message": "ok"}


@router.post('/products', tags=["products"], response_model=ProductOUT, status_code=status.HTTP_201_CREATED)
def cadastrar_produto(produto: ProductIN):
  '''cadastrar um novo produto'''
  novo_produto = insert_product__db(db_client, produto.name, produto.description, produto.price, produto.quantity)
  return novo_produto


@router.get("/products", tags=["products"], response_model=ProductsDB)
def pegar_produtos():
  '''pegar todos os produtos'''
  return { "products" : get_all_products_db(db_client) }


@router.get("/products/{id}", tags=["products"], response_model=ProductOUT)
def pegar_produto_id(id: int):
  '''pegar produto pelo seu identificador'''
  product = get_product_by_id_db(db_client, id)
  if product is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
  return product


@router.put("/products/{id}", tags=["products"], response_model=ProductOUT)
def update_produto(id: int, prod: ProductIN):
  '''atualizando dados de um produto do banco'''
  sucess = update_product_db(db_client, id, prod.name, prod.description, prod.price, prod.quantity)
  if not sucess:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="product not found")
  return sucess


@router.delete("/products/{id}", tags=["products"], status_code=status.HTTP_204_NO_CONTENT)
def deletar_produto(id: int):
  '''deletando um produto do banco'''
  sucess = delete_product_db(db_client, id)
  if not sucess:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="product not found")
  return None