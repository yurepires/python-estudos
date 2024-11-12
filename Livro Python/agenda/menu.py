class Menu:
    def __init__(self):
        self.opcoes = [["Sair", None]]
    def adicionaopcao(self, nome, funcao):
        self.opcoes.append([nome, funcao])
    def exibe(self):
        print("====")
        print("Menu")
        print("====\n")
        for i, opcao in enumerate(self.opcoes):
            print(f"[{i}] - {opcao[0]}")
        print()