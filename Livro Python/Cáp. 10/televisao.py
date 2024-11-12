class Televisao:
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = 2
        self.cmin = min
        self.cmax = max
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin
tv = Televisao(1, 10)
tv2 = Televisao()
tv3 = Televisao(min=3, max=33)
print(f'Tv min = {tv.cmin} / max = {tv.cmax}')
print(f'Tv 2 min = {tv2.cmin} / max = {tv2.cmax}')
print(f'Tv 3 min = {tv3.cmin} / max = {tv3.cmax}')
tv.canal = 10
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
print(tv.canal)