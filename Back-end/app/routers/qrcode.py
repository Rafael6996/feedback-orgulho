
#← Rota que gera o QR Code (GET /api/qrcode/{id})

from fastapi import APIRouter
from fastapi.responses import FileResponse
# FileResponse é necessário pra devolver a imagem do QR Code gerada como resposta da rota

import qrcode
# Biblioteca que gera o QR Code em si

import os
# Usado pra montar o caminho onde a imagem do QR Code vai ser salva antes de devolver