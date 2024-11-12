def linha(linha="="):
    return linha * 42

def menu(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    print(opcoes(['adicionar','salvar', 'excluir', 'gravar', 'ler']))

def opcoes(lista):
    for e, i in enumerate(lista):
         print(f"{e + 1} - {i}")
    return linha()