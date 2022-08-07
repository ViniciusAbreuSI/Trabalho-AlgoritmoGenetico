from individuo import Individuo
from random import randint

class Population:
    """
    Classe que representa a populacao.
    """
    def __init__(self, individualsInitialNumber, minX=None, maxX=None):
        """
        Construtor da classe que representa a populacao.
        """
        self.individuals = [] if individualsInitialNumber == 0 else [Individuo(randint(minX, maxX)) for _ in range(individualsInitialNumber)]

