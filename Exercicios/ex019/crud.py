import sqlite3
from pathlib import Path

NOME_BANCO = "cadastro.db"
caminho_banco = Path(__file__).parent / NOME_BANCO

def criar_banco() -> bool:
    try:
        
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
def cadastro_em_massa():
    cad_pessoas = [
        ("1", "Paulo", "1.85"),
        ("2", "Maria", "1.70"),
        ("3", "João", "1.75"),
        ("4", "Ana", "1.60"),
        ("5", "Carlos", "1.80"),
        ("6", "Fernanda", "1.65"),
        ("7", "Ricardo", "1.90"),
        ("8", "Juliana", "1.68"),
        ("9", "Marcos", "1.78"),
        ("10", "Patrícia", "1.72")
    ]
    
    try:
        with sqlite3.connect(caminho_banco) as db:
            cursor = db.cursor()
            cursor.executemany('''
                INSERT INTO pessoas (cod, nome, altura)
                VALUES (?, ?, ?)
            ''', cad_pessoas)
            db.commit()
            print("Dados inseridos em massa com sucesso.")
        
    except sqlite3.Error as e:
        print(f"Erro ao inserir dados em massa: {e}")
        # return False
    
def cadastrar_usuario() -> bool:
    print("\nCADASTRO DE USUÁRIO")
    
    # Leitura e Validacao
    nome = input("Digite o nome do usuário: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        # return False
    altura = input("Digite a altura do usuário: ").strip().replace(",", ".")
    if not altura:
        print("Altura não pode ser vazia.")
        #return False

    try:
        altura = float(altura)
        if altura <= 0.30 or altura >= 3.00:
            print("Altura inválida. Digite um valor entre 0.30 e 3.00 metros.")
            return False
    except ValueError:
        print("[ERRO] Altura inválida. Digite um número.")
        return False

    # Cadastra Usuario
    try:
        with sqlite3.connect(caminho_banco) as db:
            cursor = db.cursor()
            cursor.execute('''
                INSERT INTO pessoas (nome, altura)
                VALUES (?, ?)
            ''', (nome, altura))
            db.commit()
            print(f"Usuário {nome} cadastrado com sucesso.")
            return True
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar usuário: {e}")
        return False

def listar_usuarios() -> list:
    pass

def atualizar_usuario() -> bool:
    pass

def excluir_usuario() -> bool:
    pass

def buscar_usuario() -> list:
    pass
