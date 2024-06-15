from fastapi import APIRouter

from store.schemas.product import ProductIn

router = APIRouter()

@router.get("/")
def root_path():
  '''root path.'''
  return {"messagem": "Hello"}

@router.post("/produtos", tags=["produtos"], response_model=ProductIn)
def cadastrar_produto(produto: ProductIn):
  '''cadastrar um novo produto.'''
  pass

@router.get("/produtos", tags=["produtos"], response_model=ProductIn)
def pegar_produtos():
  '''pegar todos os produtos.'''
  pass

@router.get("/produtos/{id}", tags=["produtos"], response_model=ProductIn)
def pegar_produto_id(id: int):
  '''pegar um produto pelo seu id.'''
  pass

@router.put("/produtos/{id}", tags=["produtos"], response_model=ProductIn)
def atualizar_produto(id: int, produto: ProductIn):
  '''atualizar um produto.'''
  pass

@router.delete("/produtos/{id}", tags=["produtos"], response_model=ProductIn)
def delete_produto(id: int):
  '''deletar um produto.'''
  pass