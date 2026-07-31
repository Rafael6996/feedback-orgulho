# ← Rotas de salas/projetos (GET, importar planilha)

from fastapi import APIRouter, UploadFile, File, Depends
# UploadFile e File são necessários especificamente pra rota que recebe a planilha enviada

from sqlalchemy.orm import Session
# Mesmo motivo do arquivo anterior — trabalhar com sessão do banco

from ..database import SessionLocal
# Abrir sessão com o banco

from ..models import Sala
# Tabela de salas/projetos do evento

from ..schemas import SalaOut
# Molde de validação pra retornar dados de sala formatados

from ..utils.planilha import processar_planilha
# Função (separada em utils) que usa Pandas pra ler a planilha enviada