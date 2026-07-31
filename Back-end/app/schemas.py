

#← Validação dos dados de entrada/saída (Pydantic)

from pydantic import BaseModel, Field
# BaseModel é a base de toda validação; Field permite regras extras (ex: min/max da nota)

from typing import Optional
# Marca campos que não são obrigatórios (ex: comentário pode vir vazio)

from datetime import datetime
# Tipo de dado pra representar data/hora (usado no campo criado_em)