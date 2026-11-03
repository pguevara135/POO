import sqlite3
from pathlib import Path

NOME_BANCO = "cadastro.db"

def criar_banco() -> bool:
    try:
        caminho_banco = Path(__file__).parent / NOME_BANCO
        with sqlite3.connect(caminho_banco) as db:
            cursor = db.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pessoas (
                    cod INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    altura REAL NOT NULL
                )
            ''')
            return True
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela: {e}")
        return False
    
def cadastrar_usuario() -> bool:
    pass

def listar_usuarios() -> list:
    pass

def atualizar_usuario() -> bool:
    pass

def excluir_usuario() -> bool:
    pass

def buscar_usuario() -> list:
    pass
