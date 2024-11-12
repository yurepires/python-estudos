from nome import Nome
from dadosagenda import DadoAgenda
from tipostelefone import TipoTelefone
from listaunica import ListaUnica
class TiposTelefone(ListaUnica):
    def __init__(self):
        super().__init__(TipoTelefone)
class Agenda(ListaUnica):
    def __init__(self):
        super().__init__(DadoAgenda)
        self.tiposTelefone = TiposTelefone()
    def adicionaTipo(self, tipo):
        self.tiposTelefone.adiciona(TipoTelefone(tipo))
    def pesquisaNome(self, nome):
        if isinstance(nome, str):
            nome = Nome(nome)
        for dados in self.lista:
            if dados.nome == nome:
                return dados
        else:
            return None
    def ordena(self):
        super().ordena(lambda dado: str(dado.nome))