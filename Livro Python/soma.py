# Programa 8.19 - Módulo soma (soma.py) que importa entrada
import entrada
l = []
for x in range(10):
    l.append(entrada.valida_inteiro('Digite um número: ', 0, 20))
print(f'Soma: {sum(l)}')