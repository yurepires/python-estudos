
tabela = [[[12.51, 13.50], 3],
          [[13.51, 14.50], 8],
          [[14.51, 15.50], 15],
          [[15.51, 16.50], 13],
          [[16.51, 17.50], 9],
          [[17.51, 18.50], 2]]

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


while True:
    print("--- CALCULO ---")
    print("1 - Percentil")
    print("2 - Decil")
    print("3 - Quartil")
    menu = input(">>> ")
    if menu == '1':
        x = int(input("Digite o percentil: "))
        x /= 100
        calculo = calculoPercentil(x, tabela)
    elif menu == '2':
        x = int(input("Digite o decil: "))
        x = (x * 10)/100
        calculo = calculoPercentil(x, tabela)
    elif(menu == '3'):
        x = int(input("Digite o quartil: "))
        x = (25 * x) / 100
        calculo = calculoPercentil(x, tabela)
    else:
        print("Opção inválida!")
    
    print("O cálculo do percentil é ", calculo)
    break