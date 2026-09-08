from pagamentos import *


def main():
    finalizar_pagamento(Boleto(), 1000)
    finalizar_pagamento(Cartao(), 5500)
    finalizar_pagamento(Pix(), 1300)

if __name__ == "__main__":
    main()
