from conta_bancaria import ContaBancaria

def main():
    c1 = ContaBancaria(100, "Paulo", 5000)
    c1.depositar(3000)
    c1.sacar(500)
        
    print(c1)

if __name__ == "__main__":
    main()