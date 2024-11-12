# Programa 9.3 - Gravação de números pares e ímpares em arquivos diferentes
with open('impares.txt', 'w') as impares:
    with open('pares.txt', 'w') as pares:
        for n in range(0, 1000):
            if n % 2 == 0:
                pares.write(f'{n}\n')
            else:
                impares.write(f'{n}\n')