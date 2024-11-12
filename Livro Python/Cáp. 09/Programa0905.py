# Programa 9.5 - Processamento de um arquivo

LARGURA = 79
with open('entrada.txt') as entrada:
    for linha in entrada.readlines():
        if linha[0] == ';':
            continue
        elif linha[0] == '>':
            print(linha[1:].rjust(LARGURA))
        elif linha[0] == '*':
            print(linha[1:].center(LARGURA))
        else:
            print(linha)
entrada.close()