#← Rotas do formulário (POST /api/respostas)

from fastapi import APIRouter, Depends, HTTPException
# APIRouter cria um "grupo" de rotas; Depends injeta a sessão do banco; HTTPException retorna erros customizados

from sqlalchemy.orm import Session
# Tipo usado pra dizer que a função recebe uma sessão ativa do banco

from ..database import SessionLocal
# Função que abre uma nova sessão de conversa com o banco a cada requisição

from ..models import Resposta
# A tabela (classe) de respostas, definida em models.py

from ..schemas import RespostaCreate, RespostaOut
# Os "moldes" de validação — um pro que entra (criar), outro pro que sai (retornar) da API