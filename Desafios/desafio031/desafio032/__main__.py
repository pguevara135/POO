from conta_bancaria import ContaBancaria

def main():
    c1 = ContaBancaria(10, "Paulo", 5000, "paulo123")
    print("\nSaque...\n")
    
    c1.sacar(500, "paulo123")
    
    print("\nTrocando o nome...\n")
    
    c1.nome = 'Julia'

if __name__ == "__main__":
    main()