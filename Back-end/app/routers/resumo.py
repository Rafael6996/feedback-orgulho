# ← Rota do resumo pro dashboard (GET /api/resumo)

from fastapi import APIRouter, Depends
# Criação de rota + injeção de sessão do banco

from sqlalchemy.orm import Session
from sqlalchemy import func
# func é necessário aqui pra fazer contas direto no banco (AVG, COUNT) sem trazer tudo pro Python

from ..database import SessionLocal
from ..models import Resposta
# Precisa da tabela de respostas pra calcular médias e totais