velocidade = float(input('Digite a velocidade: '))
velocidae_maxima = 80

if velocidade <= velocidae_maxima:
    print('Nao houve multa')
elif velocidade <= velocidae_maxima + 10:
    print('Multa leve')
elif velocidade <= velocidae_maxima + 20:
    print("Multa grave")
else:
    print('Multa gravissima') 

import pdb

def divide(a, b):
    pdb.set_trace()
    return a / b

print(divide(10, 2))