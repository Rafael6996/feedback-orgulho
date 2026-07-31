import pandas as pd
# Lê e processa a planilha (Excel ou CSV) enviada pelo formulário de importação

from io import BytesIO
# Necessário porque o arquivo chega "em memória" (upload), não como um caminho físico no disco
#← Função que lê a planilha com Pandas