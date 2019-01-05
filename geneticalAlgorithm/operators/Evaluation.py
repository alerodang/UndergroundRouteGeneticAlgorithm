class Evaluator:

    def __init__(self, journeys):
        self.__journeys = journeys

    def evaluate(self, individuals):

        for individual in individuals:
            individual.fitnessValue = self.evaluateIndividual(individual)

    def evaluateIndividual(self, individual):

        fitnessValue = 0

        for i in range(0, len(individual.genes) - 1):
            fitnessValue += self.__journeys[individual.genes[i]][individual.genes[i + 1]]

        return fitnessValue