from listaunica import ListaUnica
from telefone import Telefone
from nome import Nome
class Telefones(ListaUnica):
    def __init__(self):
        super().__init_(Telefone)
class DadoAgenda:
    def __init_(self, nome):
        self.nome = nome
        self.telefones = Telefones()
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, Nome):
            raise TypeError("nome deve ser uma instância da classe nome")
        self.__nome = valor
    def pesquisaTelefone(self, telefone):
        posicao = self.telefones.pesquisa(Telefone(telefone))
        if posicao == -1:
            return None
        else:
            return self.telefones[posicao]