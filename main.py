from algoritmoGenetico import Algorithm

def main():
    """
    Função que le as entradas do usuario e executa o algoritmo.
    """
    option = input('Deseja customizar os dados? [S/N] ')

    if option == 'S':
        individualsInitialNumber = int(input('Qual numero inicial de individuos? [Entre com um numero inteiro] '))

        generationQuantity = int(input('Qual numero de geracoes? [Entre com um numero inteiro] '))
        
        crossoverRate = float(input('Qual taxa de crossover? [Entre com um numero entre 0 e 1] '))
        
        mutationRate = float(input('Qual taxa de mutacao? [Entre com um numero entre 0 e 1] '))
        
        populationSize = int(input('Qual tamanho maximo da populacao? [Entre com um numero inteiro] '))

        algorithm = Algorithm(individualsInitialNumber, generationQuantity, crossoverRate, mutationRate, populationSize)
    else:
        algorithm = Algorithm()

    algorithm.run()

if __name__ == '__main__':
    main()