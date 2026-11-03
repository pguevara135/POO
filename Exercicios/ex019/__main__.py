from crud import *


def exibir_menu():
    print("\n" + "=" * 30)
    print("      SISTEMA DE CADASTRO")
    print("*" * 30)
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários cadastrados")
    print("3 - Atualizar informações de um usuário")
    print("4 - Excluir um usuário")
    print("5 - Buscar usuário por nome")
    print("0 - Sair")
    
def main():
    
    if not criar_banco():
        print("Falha ao criar o banco de dados. Encerrando o programa.")
        raise SystemExit
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        match opcao:
            case "1":
                if not cadastrar_usuario():
                    print("\n[ERRO]Falha ao cadastrar o usuário.")
            case "2":
                if not listar_usuarios():
                    print("\n[ERRO]Falha ao listar os usuários.")
            case "3":
                if not atualizar_usuario():
                    print("\n[ERRO]Falha ao atualizar o usuário.")
            case "4":
                if not excluir_usuario():
                    print("\n[ERRO]Falha ao excluir o usuário.")
            case "5":
                if not buscar_usuario():
                    print("\n[ERRO]Falha ao buscar o usuário.")
                
            case "0":
                print("\nSaindo do sistema...")
                break
            case _:
                print("\nOpção inválida. Tente novamente. Escolha o valor entre 0 e 5")
        
        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()