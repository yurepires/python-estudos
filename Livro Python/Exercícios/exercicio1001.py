# Exercício 10.1
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.polegadas = None
        self.marca = None
tv = Televisao()
tv.polegadas = 32
tv.marca = 'TCL'
tv_sala = Televisao()
tv_sala.canal = 5
tv_sala.ligada = True
tv_sala.polegadas = 65
tv_sala.marca = 'LG'
print(f"tv tamanho={tv.polegadas} marca={tv.marca}")
print(f"tv_sala tamanho={tv_sala.polegadas} marca={tv_sala.marca}")