import sqlite3
from datetime import datetime
 
NOME_BANCO = "mapa.db"
 
# Nomes dos campos esperados vindos do formulário
CAMPOS_FORMULARIO = ["nome", "latitude", "longitude", "descricao", "categoria"]
 
 
def conectar(nome_banco: str = NOME_BANCO) -> sqlite3.Connection:
    """Abre (ou cria) a conexão com o banco de dados SQLite."""
    conexao = sqlite3.connect(nome_banco)
    conexao.row_factory = sqlite3.Row
    return conexao
 
 
def criar_tabela(conexao: sqlite3.Connection) -> None:
    """Cria a tabela de pontos do mapa, caso ainda não exista."""
    conexao.execute(
        """
        CREATE TABLE IF NOT EXISTS pontos_mapa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            descricao TEXT,
            categoria TEXT,
            criado_em TEXT NOT NULL
        )
        """
    )
    conexao.commit()
 
 
def validar_dados(dados_formulario: dict) -> dict:
    """
    Valida e converte os dados recebidos do formulário.
    Lança ValueError se algo obrigatório estiver ausente ou inválido.
    """
    nome = (dados_formulario.get("nome") or "").strip()
    if not nome:
        raise ValueError("O campo 'nome' é obrigatório.")
 
    try:
        latitude = float(dados_formulario.get("latitude"))
        longitude = float(dados_formulario.get("longitude"))
    except (TypeError, ValueError):
        raise ValueError("Latitude e longitude devem ser números válidos.")
 
    if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
        raise ValueError("Latitude/longitude fora do intervalo válido.")
 
    descricao = (dados_formulario.get("descricao") or "").strip()
    categoria = (dados_formulario.get("categoria") or "").strip()
 
    return {
        "nome": nome,
        "latitude": latitude,
        "longitude": longitude,
        "descricao": descricao,
        "categoria": categoria,
    }
 
 
def salvar_ponto_do_formulario(dados_formulario: dict, nome_banco: str = NOME_BANCO) -> int:
    """
    Recebe um dicionário com os dados do formulário (ex: request.form),
    valida e insere um novo ponto de mapa no banco de dados.
 
    Retorna o id do registro inserido.
    """
    dados = validar_dados(dados_formulario)
 
    conexao = conectar(nome_banco)
    try:
        criar_tabela(conexao)
        cursor = conexao.execute(
            """
            INSERT INTO pontos_mapa (nome, latitude, longitude, descricao, categoria, criado_em)
            VALUES (:nome, :latitude, :longitude, :descricao, :categoria, :criado_em)
            """,
            {**dados, "criado_em": datetime.now().isoformat(timespec="seconds")},
        )
        conexao.commit()
        return cursor.lastrowid
    finally:
        conexao.close()
 
 
def listar_pontos(nome_banco: str = NOME_BANCO) -> list[dict]:
    """Retorna todos os pontos de mapa salvos no banco."""
    conexao = conectar(nome_banco)
    try:
        criar_tabela(conexao)
        linhas = conexao.execute("SELECT * FROM pontos_mapa ORDER BY id").fetchall()
        return [dict(linha) for linha in linhas]
    finally:
        conexao.close()
 
 
if __name__ == "__main__":
    # Exemplo de uso: simula dados que viriam de um formulário real
    dados_exemplo = {
        "nome": "Marco Zero",
        "latitude": "-8.0631",
        "longitude": "-34.8711",
        "descricao": "Ponto histórico no Recife Antigo",
        "categoria": "ponto turístico",
    }
 
    id_inserido = salvar_ponto_do_formulario(dados_exemplo)
    print(f"Ponto salvo com sucesso! id={id_inserido}")
 
    print("\nPontos atualmente no banco:")
    for ponto in listar_pontos():
        print(ponto)