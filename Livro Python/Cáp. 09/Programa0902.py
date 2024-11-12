# Programa 9.2 - Uso do with
with open('numeros.txt', 'r') as arquivo:
    for linha in arquivo.readlines():
        print(linha)