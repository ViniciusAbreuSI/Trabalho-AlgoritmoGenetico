from individuo import Individuo
from populacao import Population
from random import randint

class Algorithm:
    """
    Classe que representa o algoritmo.
    """
    def __init__(self, individualsInitialNumber=4, generationQuantity=5, crossoverRate=0.7, mutationRate=0.01, populationSize=30):
        """
        Construtor da classe.
        """
        self.individualsInitialNumber = individualsInitialNumber
        self.minX = -10
        self.maxX = 10
        self.population = Population(self.individualsInitialNumber, self.minX, self.maxX)
        self.crossoverRate = crossoverRate
        self.mutationRate = mutationRate
        self.generationQuantity = generationQuantity
        minX_bit_number = len(self.convertDecimalToBinary(self.minX))
        maxX_bit_number = len(self.convertDecimalToBinary(self.maxX))
        self.number_of_bits = minX_bit_number if minX_bit_number > maxX_bit_number else maxX_bit_number
        self.populationSize = populationSize
    
    def bestIndividual(self):
        """
        Metodo que retorna o melhor individuo da populacao.
        """
        return min(self.population.individuals, key=lambda individual: individual.fitnessFunctionResult)
    
    def convertBinaryToDecimal(self, numberAsBinary):
        """
        Metodo que converte um valor em binario para decimal.
        """
        return int(''.join(numberAsBinary), 2)

    def convertDecimalToBinary(self, numberAsDecimal):
        """
        Metodo que converte um valor em decimal para binario.
        """
        return bin(numberAsDecimal).replace('0b', '' if numberAsDecimal < 0 else '+')

    def evaluate(self):
        """
        Metodo que avalia todos os individuos da populacao a partir da funcao
        fitness.

        f(x) = x^2 - 3 * x + 4
        """
        for individual in self.population.individuals:
            fitnessFunctionResult = individual.numberAsDecimal ** 2 - 3 * individual.numberAsDecimal + 4

            individual.fitnessFunctionResult = fitnessFunctionResult
    
    def select(self):
        """
        Metodo que seleciona um individuo aleatoriamente na populacao.
       
        """
        index_1 = randint(0, len(self.population.individuals) - 1)

        index_2 = randint(0, len(self.population.individuals) - 1)

        individual_1 = self.population.individuals[index_1]

        individual_2 = self.population.individuals[index_2]

        return individual_1 if individual_1.fitnessFunctionResult <= individual_2.fitnessFunctionResult else individual_2
    
    def crossover(self, parent_1, parent_2):
        """
        Metodo que realiza o crossover entre dois individuos e retorna dois
        filhos desses individuos. 
        """
        if randint(0, 1) <= self.crossoverRate:
            cut = randint(1, self.number_of_bits)

            individual_1_as_binary = parent_1.numberAsBinary[:cut] + parent_2.numberAsBinary[cut:]

            individual_2_as_binary = parent_2.numberAsBinary[:cut] + parent_1.numberAsBinary[cut:]

            individual_1 = Individuo(self.convertBinaryToDecimal(individual_1_as_binary))

            individual_2 = Individuo(self.convertBinaryToDecimal(individual_2_as_binary))

            self.adjust(individual_1)

            self.adjust(individual_2)
        else:
            individual_1 = Individuo(parent_1.numberAsDecimal)

            individual_2 = Individuo(parent_2.numberAsDecimal)

        return (individual_1, individual_2)

    def adjust(self, individual):
        """
        Metodo para ajustar o individuo. 
        """
        need_to_adjust = False

        if individual.numberAsDecimal < self.minX:
            new_decimal = self.minX

            new_binary = self.convertDecimalToBinary(new_decimal)

            need_to_adjust = True
        elif individual.numberAsDecimal > self.maxX:
            new_decimal = self.maxX

            new_binary = self.convertDecimalToBinary(new_decimal)
        
            need_to_adjust = True

        if need_to_adjust:
            individual.numberAsDecimal = new_decimal

            individual.numberAsBinary = new_binary

    def mutation(self, individual):
        """
        Metodo que realiza a mutacao de um individuo a uma taxa pre-determinada.
        """
        if randint(0, 1) <= self.mutationRate:
            bit = randint(0, self.number_of_bits - 1)

            new_binary = ''

            for i in range(len(individual.numberAsBinary)):
                if bit == 0 and i == 0:
                    new_binary += '+' if individual.numberAsBinary[bit] == '-' else '-'
                elif bit == i:
                    new_binary += '1' if individual.numberAsBinary[bit] == '0' else '0'
                else:
                    new_binary += individual.numberAsBinary[i]

            new_decimal = self.convertBinaryToDecimal(new_binary)

            new_individual = Individuo(new_decimal)

            self.adjust(new_individual)

            return new_individual
        
        return individual
    
    def run(self):
        """
        Metodo que executa o algoritmo. 
        """
        self.evaluate()

        for i in range(self.generationQuantity):
            print(f'Resultado da geracao {i}: {self.bestIndividual()}')

            new_population = Population(0)

            sorted_population = sorted(self.population.individuals, key=lambda individual: individual.fitnessFunctionResult)

            cut_to_elitism = int(len(self.population.individuals) * 0.3)

            new_population.individuals = sorted_population[:cut_to_elitism]

            while len(new_population.individuals) < self.populationSize:
                parent_1 = self.select()

                parent_2 = self.select()

                individual_1, individual_2 = self.crossover(parent_1, parent_2)

                if individual_1:
                    individual_1 = self.mutation(individual_1)

                    new_population.individuals.append(individual_1)

                if individual_2:
                    individual_2 = self.mutation(individual_2)

                    new_population.individuals.append(individual_2)
            
            self.population = new_population

            self.evaluate()

        print(f'Resultado da geracao {i + 1}: {self.bestIndividual()}')
