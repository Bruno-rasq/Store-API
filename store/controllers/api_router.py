from fastapi import APIRouter

# DB - metodos
from store.db.db_products import get_all_products_db, get_product_by_id_db
from store.db.db_products import insert_product__db
from store.db.db_products import update_product_db
from store.db.db_products import delete_product_db

# models 
from store.schemas.product import ProductIN


router = APIRouter()


@router.get("/")
def root_path():
  return {"message": "ok"}


@router.get("/products", tags=["products"])
def pegar_produtos():
  return get_all_products_db()


@router.get("/products/{id}", tags=["products"])
def pegar_produto_id(id: int):
  try:
    produto = get_product_by_id_db(id)
    return produto
  except Exception as err:
    raise err


@router.post('/products', response_model=ProductIN, tags=["products"])
def cadastrar_produto(produto: ProductIN):
  insert_product__db(produto.name, produto.description, produto.price, produto.quantity)
  return produto


@router.delete("/products/{id}", tags=["products"])
def deletar_produto(id: int):
  delete_product_db(id)


@router.put("/products/{id}", tags=["products"])
def update_produto(id: int, prod: ProductIN):
  update_product_db(id, prod.name, prod.description, prod.price, prod.quantity)