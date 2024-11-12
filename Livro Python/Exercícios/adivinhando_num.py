''' Programa 8.20
import random
n = random.randint(1, 10)
try:
    x = int(input('Escolha um número entre 1 e 10: '))
    if x == n:
        print('Você acertou!')
    else:
        print('Você errou!')
except ValueError:
    print('Digite um número inteiro!')
finally:
    print(f'O número sorteado foi: {n}') '''

# Exercício 8.13
import random
import os
n = random.randint(1, 10)
z = 0
try:
    while z < 3:
        x = int(input('Escolha um número entre 1 e 10: '))
        if x == n:
            print('Você acertou!')
            os.system('pause')
            break
        else:
            print('Você errou!')
        z += 1
except 0 < x < 10:
    print("Digite um número entre 1 e 10!")
except ValueError:
    print('Digite um número inteiro!')
finally:
    print(f'O número sorteado foi: {n}')
    os.system('pause')