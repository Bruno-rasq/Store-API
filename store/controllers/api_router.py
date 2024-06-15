from typing import List
from fastapi import APIRouter, HTTPException
from store.schemas.product import ProductIn, ProductOUT
from store.db.services_db import cadastrar_produto_db, get_produtos_db

router = APIRouter()

@router.get("/")
def root_path():
  '''root path.'''
  return {"messagem": "Hello"}



@router.post("/produtos", tags=["produtos"], response_model=ProductOUT)
def cadastrar_produto(produto: ProductIn):
  '''cadastrar um novo produto.'''
  try:
    novo_produto = cadastrar_produto_db(produto)
    return novo_produto
  except Exception as err:
    HTTPException(status_code=500, detail=str(err))



@router.get("/produtos", tags=["produtos"], response_model=List[ProductOUT])
def pegar_produtos():
  '''pegar todos os produtos.'''
  return get_produtos_db()
  

# @router.get("/produtos/{id}", tags=["produtos"], response_model=ProductIn)
# def pegar_produto_id(id: int):
#   '''pegar um produto pelo seu id.'''
#   pass

# @router.put("/produtos/{id}", tags=["produtos"], response_model=ProductIn)
# def atualizar_produto(id: int, produto: ProductIn):
#   '''atualizar um produto.'''
#   pass

# @router.delete("/produtos/{id}", tags=["produtos"], response_model=ProductIn)
# def delete_produto(id: int):
#   '''deletar um produto.'''
#   pass