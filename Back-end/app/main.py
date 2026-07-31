# Ponto de entrada, cria o FastAPI e as rotas
from fastapi import FastAPI
# Classe principal que cria a aplicação/servidor

from fastapi.middleware.cors import CORSMiddleware
# Libera o frontend (GitHub Pages) a fazer requisições pro backend sem ser bloqueado

from .routers import respostas, salas, resumo, qrcode
# Importa cada arquivo de rota separado, pra "plugar" no app principal

from .database import engine, Base
# engine conecta ao banco; Base.metadata.create_all(engine) cria as tabelas se não existirem