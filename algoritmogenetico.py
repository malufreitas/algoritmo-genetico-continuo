'''
1. Gerar a população inicial.
2. Avaliar cada indivíduo da população.
3. Enquanto critério de parada não for satisfeito
faça
3.1 Selecionar os indivíduos mais aptos.
 3.2 Criar novos indivíduos aplicando os
 operadores crossover e mutação.
 3.3 Armazenar os novos indivíduos em uma
 nova população.
 3.4 Avaliar cada indivíduo da nova
 população.

 Função aptidao:
 f (x)=cos(x)∗x+2
'''

from Cromossomo import Cromossomo
import random
import copy

def mutacao(filho):
    taxaMutacao = random.uniform(0, 1)
    if(taxaMutacao <= 0.05):
        gene = random.uniform(0, 1)
        if gene < 0.5:
            filho.set_valorcontinuo(-20)
        else:
            filho.set_valorcontinuo(20)
    return filho

def crossover(cromossomoA, cromossomoB):
    #  Operador BLX-alpha
    pai1 = cromossomoA.get_valorcontinuo()
    pai2 = cromossomoB.get_valorcontinuo()
    alpha = 0.5
    beta = random.uniform(alpha,1+alpha)

    f1 = pai1 + beta*(pai2-pai1)
    if (f1 < -20):
        f1 = -20
    elif (f1 > 20):
        f1 = 20
    else:
        f1 = f1
    filho1 = Cromossomo(f1)

    f2 = pai1 + beta*(pai2-pai1)
    if (f2 < -20):
        f2 = -20
    elif (f2 > 20):
        f2 = 20
    else:
        f2 = f2
    filho2 = Cromossomo(f2)
    
    return filho1, filho2

def gera_populacao_inicial(numero_populacao):
    lista_populacao = []

    for _ in range(numero_populacao):
        valor_continuo = random.uniform(-20, 20)
        cromossomo = Cromossomo(valor_continuo)
        lista_populacao.append(cromossomo)

    return lista_populacao

def algoritmo_genetico(numero_populacao, geracoes):
    # Lista para armazenar os resultados para o gráfico
    # Guarda a melhor aptidao de Cada nova iteração
    lista_melhor_aptidao = []

    # Definicao da populacao inicial
    lista_populacao = gera_populacao_inicial(numero_populacao)

    for _ in range(geracoes):
        lista_selecionados = []

        for i in range(len(lista_populacao)):
            # Aleatoriamente escolhe dois cromossomos para comparar
            # posicao_Aleatoria = random.randint(0, len(lista_populacao)-1)
            posicao_Aleatoria = i
            cromossomo_1 = copy.deepcopy(lista_populacao[posicao_Aleatoria])

            posicao_Aleatoria = random.randint(0, len(lista_populacao)-1)
            cromossomo_2 = copy.deepcopy(lista_populacao[posicao_Aleatoria])

            # Compara qual cromossomo é o melhor (menor aptidao)
            if cromossomo_1.get_aptidao() < cromossomo_2.get_aptidao():
                lista_selecionados.append(cromossomo_1)
            else:
                lista_selecionados.append(cromossomo_2)

        lista_populacao_nova = []

        for i in range(0, len(lista_selecionados), 2):
            cromossomoA = lista_selecionados[i]
            cromossomoB = lista_selecionados[i+1]

            # Crossover
            taxaCrossover = random.uniform(0, 1)
            if(taxaCrossover <= 0.6):
                filho1, filho2 = crossover(cromossomoA, cromossomoB)
            else:
                filho1, filho2 = cromossomoA, cromossomoB

            # Mutação
            filho1 = mutacao(filho1)
            filho2 = mutacao(filho2)

            # Inserção na nova população
            lista_populacao_nova.append(filho1)
            lista_populacao_nova.append(filho2)

        # Ordenação dos filhos em ordem crescente de aptidão
        lista_populacao_nova = sorted(lista_populacao_nova, key=Cromossomo.get_aptidao)

        piorFilho = lista_populacao_nova[-1]

        # Ordenação dos pais em ordem crescente de aptidão
        lista_populacao = sorted(lista_populacao, key=Cromossomo.get_aptidao)
        melhor_pai = lista_populacao[0]

        if (piorFilho.get_aptidao() > melhor_pai.get_aptidao()):
            # Removendo o pior filho
            for i in range(len(lista_populacao_nova)):
                if lista_populacao_nova[i].get_aptidao() == piorFilho.get_aptidao():
                    del lista_populacao_nova[i]
                    break

            # E mantendo o melhor pai da população anterior para a próxima geração
            lista_populacao_nova.append(melhor_pai)

        lista_populacao_nova = sorted(lista_populacao_nova, key=Cromossomo.get_aptidao)
        lista_melhor_aptidao.append(lista_populacao_nova[0])

        lista_populacao = lista_populacao_nova

    return lista_melhor_aptidao
