class Individuo:
    """
    Classe que representa o individuo.
    """
    def __init__(self, numberAsDecimal):
        """
        Construtor da classe.
        """
        self.numberAsDecimal = numberAsDecimal
        self.numberAsBinary = bin(self.numberAsDecimal).replace('0b', '' if self.numberAsDecimal < 0 else '+')
        self.fitnessFunctionResult = float('inf')

    def __repr__(self):
        """
        Sobrescrita do metodo de representacao da classe.
        """
        return f'{self.numberAsDecimal} | {self.fitnessFunctionResult}'
