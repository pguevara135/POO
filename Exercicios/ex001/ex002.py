import sys
def print_python_version():
    print(sys.version)

tipo = input('Digite algo: ')

print('O tipo primitivo e: ', type(tipo))
print('Somente espaco ', tipo.isspace())
print('E um numero? ', tipo.isnumeric())
print('E alfabetico? ', tipo.isalpha())
print('E alfanumerico? ', tipo.isalnum())
print('Esta em maiuscula? ', tipo.isupper())
print('Esta em minuscula? ', tipo.islower())
print('Esta capitalizada? ', tipo.istitle())
