import os

tabela = [[[12.51, 13.50], 3],
          [[13.51, 14.50], 8],
          [[14.51, 15.50], 15],
          [[15.51, 16.50], 13],
          [[16.51, 17.50], 9],
          [[17.51, 18.50], 2]]

def ordenaTabela(tabela):
    numerosOrdenados = []
    for classe in tabela:
        i = 0
        while i < classe[1]:
            numerosOrdenados.append((classe[0][0] + classe[0][1]) / 2)
            i += 1
    return numerosOrdenados

def pontoMedio(tabela):
    pontoMedioClasses = []
    i = 0
    while i < len(tabela):
        pontoMedioClasses.append((tabela[i][0][0] + tabela[i][0][1]) / 2) 
        i += 1
    return pontoMedioClasses

def media(tabela):
    pontoMedioClasses = pontoMedio(tabela)
    media = 0
    i = 0
    while i < len(tabela):
        media += pontoMedioClasses[i] * tabela[i][1]
        i += 1
    media = media / somaFrequencias(tabela)
    return media

def moda(tabela):
    maior = 0
    pegaModa = []
    i = 0
    while i < len(tabela):
        if(tabela[i][1] > maior):
            maior = tabela[i][1]
            pegaModa = tabela[i]
        i += 1
    return pegaModa

def mediana(tabela):
    elementosOrdenados = ordenaTabela(tabela)
    meio = somaFrequencias(tabela) / 2
    if(meio % 1 == 0):
        meio += 0.5
        pegaMediana = elementosOrdenados[int(meio)]
        return pegaMediana
    else:
        pegaMediana = (elementosOrdenados[meio] + elementosOrdenados[meio + 1]) / 2
        return pegaMediana
        
def desvioPadrao(tabela):
    mediaTabela = media(tabela)
    elementosOrdenados = pontoMedio(tabela)
    calculoDesvioPadrao = 0
    i = 0
    while i < len(elementosOrdenados):
        calculoDesvioPadrao += (elementosOrdenados[i] - mediaTabela) ** 2
        i += 1
    calculoDesvioPadrao = calculoDesvioPadrao / (len(tabela) - 1)
    return calculoDesvioPadrao

def somaFrequencias(tabela, iteraAte=len(tabela)):
    soma = 0
    i = 0
    while i < iteraAte:
        soma += tabela[i][1]
        i += 1
    return soma

def descobreClasse(x, tabela):
    elementoProcurado = x * somaFrequencias(tabela)
    buscaClasse = 0
    i = 0
    while(i < len(tabela)):
        buscaClasse += tabela[i][1]
        if(buscaClasse >= elementoProcurado):
            return i
        i += 1

def calculoPercentil(x, tabela):
    indiceClasse = descobreClasse(x, tabela)
    classePercentil = tabela[indiceClasse]
    limiteInferior =  classePercentil[0][0]
    amplitudeClasse = classePercentil[0][1] - classePercentil[0][0]
    somaFrequenciasAnteriores = somaFrequencias(tabela, indiceClasse)
    calculo = limiteInferior + ((x * somaFrequencias(tabela) - somaFrequenciasAnteriores) * amplitudeClasse) / classePercentil[1]
    return calculo


def imprimeOperacaoEscolhida(menu):
    if menu == '1' or menu == 100:
        return "percentil"
    elif menu == '2' or menu == 10:
        return "decil"
    elif menu == '3' or menu == 3:
        return "quartil"

def retornaX(til):
    while True:
        x = int(input("Digite o %s: " % (imprimeOperacaoEscolhida(til))))
        if(x > 0 and x <= til):
            return x
        else:
            print("%s inválido! Digite um percentil válido." % (imprimeOperacaoEscolhida(til)))
            continue

while True:
    os.system("cls")
    print("média:  %s" % media(tabela))
    print("moda: %s" % moda(tabela)[0])
    print("mediana: %.3f" % mediana(tabela))
    print("desvio padrão: %.3f" % desvioPadrao(tabela))
    print("--- CALCULO ---")
    print("1 - Percentil")
    print("2 - Decil")
    print("3 - Quartil")
    menu = input(">>> ")
    if menu == '1':
        x = retornaX(100)
        x /= 100
        calculo = calculoPercentil(x, tabela)
    elif menu == '2':
        x = retornaX(10)
        x = (x * 10)/100
        calculo = calculoPercentil(x, tabela)
    elif(menu == '3'):
        x = retornaX(3)
        x = (25 * x) / 100
        calculo = calculoPercentil(x, tabela)
    else:
        print("Opção inválida!")
        os.system('pause')
        continue

    print("O cálculo do %s é: %f" % (imprimeOperacaoEscolhida(menu), calculo))
    break