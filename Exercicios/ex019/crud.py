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
    print("\nLISTA DE USUÁRIOS CADASTRADOS")
    try:
        with sqlite3.connect(caminho_banco) as db:
            cursor = db.cursor()
            cursor.execute('SELECT cod, nome, altura FROM pessoas ORDER BY nome')
            primeiro =cursor.fetchone()
            if not primeiro:
                print("[AVISO] Nenhum usuário cadastrado.")
                return True
            
            print(f"\n" + "=" * 48)
            print(f"{'COD':<6} {'NOME':<28} {'ALTURA':>8}")
            print("-" * 48)
            
            vcod, vnome, valtura = primeiro
            print(f"{vcod:<6} {vnome:<28} {valtura:>8.2f} mt")
            
            for vcod, vnome, valtura in cursor:
                print(f"{vcod:<6} {vnome:<28} {valtura:>8.2f} mt")
                
            print("\n" + "=" * 48)
            
            return True
    except sqlite3.Error as e:
        print(f"Erro ao listar usuários: {e}")
        return False

def atualizar_usuario() -> bool:
    #? Listar usuarios cadastrados
    print("\nATUALIZAÇÃO DE USUÁRIO")
    
    listar_usuarios()
    
    #? Perguntar o ID de atualização
    atualizar_usuario = input("Digite o código do usuário que deseja atualizar: ").strip()
    if not atualizar_usuario.isdigit():
        print("Código inválido. Digite um número inteiro.")
        return False
    
    #? Buscar se o nome da pessoa existe
    vcod = int(atualizar_usuario)
    
    try:
        with sqlite3.connect(caminho_banco) as db:
            cursor = db.cursor()
            cursor.execute('SELECT nome, altura FROM pessoas WHERE cod = ?', (vcod,))
            pessoa = cursor.fetchone()
            
            if not pessoa:
                print(f"[AVISO] Nenhum usuário encontrado com o código {vcod}.")
                return False
            
            vnome, valtura = pessoa
            print(f"\nUsuário encontrado: {vnome}, Altura: {valtura:.2f} mt")
            
        #? Perguntar os novos dados

            novo_dado = input("\nDigite o que deseja atualizar (1 - Nome, 2 - Altura): ").strip()
            if novo_dado not in ["1", "2"]:
                print("Opção inválida. Digite 1 para Nome ou 2 para Altura.")
                return False
            
            if novo_dado == "1":
                novo_nome = input("Digite o novo nome: ").strip()
                if not novo_nome:
                    print("Nome não pode ser vazio.")
                    return False
                cursor.execute('UPDATE pessoas SET nome = ? WHERE cod = ?', (novo_nome, vcod))
                print(F"\nUsuário {vnome} atualizado com sucesso para {novo_nome}.")
                return True
               
            else:
                nova_altura = input("Digite a nova altura: ").strip().replace(",", ".")
                if not nova_altura:
                    print("Altura não pode ser vazia.")
                    return False
                try:
                    nova_altura = float(nova_altura)
                    if nova_altura <= 0.30 or nova_altura >= 3.00:
                        print("Altura inválida. Digite um valor entre 0.30 e 3.00 metros.")
                        return False
                    cursor.execute('UPDATE pessoas SET altura = ? WHERE cod = ?', (nova_altura, vcod))
                    print(F"\nUsuário {vnome} com altura de {valtura:.2f} mt atualizado com sucesso para altura {nova_altura:.2f} mt.")
                    # db.commit()
                    return True
                except ValueError:
                    print("[ERRO] Altura inválida. Digite um número.")
                    return False
                
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar usuario: {e}")
        return False

def excluir_usuario() -> bool: #! Excluir Pessoas
    #? Listar usuarios cadastrados
    
    print("\nEXCLUSÃO DE USUÁRIO")
    
    listar_usuarios()
    
    #? Perguntar o ID de exclusao
    
    entrada_cod = input("Digite o código do usuário que deseja excluir: ").strip()
    if not entrada_cod.isdigit():
        print("Código inválido. Digite um número inteiro.")
        return False
    
    #? Buscar se o nome da pessoa existe
    
    vcod = int(entrada_cod)
    
    
    #? Mostrar os dados da pessoa
    try:
        with sqlite3.connect(caminho_banco) as db:
            cursor = db.cursor()
            cursor.execute('SELECT nome, altura FROM pessoas WHERE cod = ?', (vcod,))
            pessoa = cursor.fetchone()
            
            if not pessoa:
                print(f"[AVISO] Nenhum usuário encontrado com o código {vcod}.")
                return False
            
            vnome, valtura = pessoa
            print(f"\nUsuário encontrado: {vnome}, Altura: {valtura:.2f} mt")
    
        #? Perguntar se deseja excluir
    
            confirmacao = input("Deseja realmente excluir este usuário? (s/n): ").strip().lower()
            
        #? Excluir a pessoa do banco de dados
    
            if confirmacao != 's':
                print("Exclusão cancelada.")
                return True
            
            cursor.execute('DELETE FROM pessoas WHERE cod = ?', (vcod,))
            print(f"Usuário {vnome} excluído com sucesso.")
            return True
    
    except sqlite3.Error as e:
        print(f"Erro ao buscar usuário: {e}")

def buscar_usuario() -> list:
    print("\nBUSCAR USUÁRIO POR NOME")
    
    termo = input("Digite o nome ou parte do nome do usuário: ")
    if not termo:
        print("Termo de busca não pode ser vazio.")
        return False
    
    try:
        with sqlite3.connect(caminho_banco) as db:
            cursor = db.cursor()
            cursor.execute('''
                SELECT cod, nome, altura FROM pessoas
                WHERE nome LIKE ?
                ORDER BY nome
            ''', (f"%{termo}%",))
            
            primeiro = cursor.fetchone()
            if not primeiro:
                print(f"[AVISO] Nenhum usuário encontrado com o {termo} informado.")
                return True
            
            print(f"\n" + "=" * 48)
            print(f"{'COD':<6} {'NOME':<28} {'ALTURA':>8}")
            print("-" * 48)
            
            vcod, vnome, valtura = primeiro
            print(f"{vcod:<6} {vnome:<28} {valtura:>8.2f} mt")
            
            for vcod, vnome, valtura in cursor:
                print(f"{vcod:<6} {vnome:<28} {valtura:>8.2f} mt")
            
            print("\n" + "=" * 48)
            return True
    
    except sqlite3.Error as e:
        print(f"Erro ao buscar usuário: {e}")
        return False
