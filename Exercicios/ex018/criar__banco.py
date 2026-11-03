import sqlite3
from pathlib import Path
from datetime import date



# conexao = sqlite3.connect(caminho_banco)

# cursor = conexao.cursor()


# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS amigos(
#                    id INTEGER PRIMARY KEY,
#                    nome TEXT NOT NULL,
#                    nascimento DATE NOT NULL
#                )
# """)

# conexao.commit()

# cursor.execute("""
#             SELECT name FROM sqlite_master WHERE type = "table"
# """)

# print(f'Banco de dados: {caminho_banco.resolve()}')
# print(f'Tabelas criadas {cursor.fetchall()}')

# conexao.close()
# cur.close()
# banco.close()

busca = input('Quem voce esta procurando? ').strip()
try:
    caminho_banco = Path(__file__).parent / "amigos.db"
    with sqlite3.connect(caminho_banco) as banco: 
        banco.row_factory = sqlite3.Row
        cur = banco.cursor()
        cur.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))

        # lista = cur.fetchall()

        total = 0
        encontrou = False
        hoje = date.today()
        
        for amigo in cur:
            encontrou = True
            total += 1
            
            txtnasc = amigo['nascimento']
            
            info_nasc = ''
            
            if not txtnasc:
                info_nasc = "Sem data de nascimento"
            
            try:
                data = date.fromisoformat(str(txtnasc))
                
                japassou = (hoje.month, hoje.day) >= (data.month, data.day)
                
                idade = hoje.year - data.year - (0 if japassou else 1)
                                
                info_nasc = f'nasceu em {data:%d/%m/%Y} e tem {idade} anos'
            except ValueError:
                info_nasc = f'Data invalida'
            
            print(f'{amigo["nome"]} {info_nasc}')
        
        print(f"-" * 30)
        if encontrou:
            if total == 1:
                print(f'Foi encontrado um amigo {busca}.')
            else:
                print(f'Ao todo foram encontrados {total} amigos com {busca}')
        else:
            print(f"Nao existe nenhum registro com o nome {busca}")

        
            
except sqlite3.Error as erro:
    print(f'Falha no banco {erro}')
except Exception as erro:
    print(f'Algo deu errado em {erro}')



print('ACABOU')
