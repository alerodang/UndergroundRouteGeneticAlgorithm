from parameters import populationSize

class Population:

    def __init__(self, origin, destiny, individualGenerator):
        self.__individualGenerator = individualGenerator
        self.individuals = self.generateIndividuals(origin, destiny)

    def generateIndividuals(self, origin, destiny):
        individuals = []
        while len(individuals) < populationSize:
            individual = self.__individualGenerator.generateIndividual(origin, destiny)
            if individual in individuals:
                continue
            individuals.append(individual)

        return individuals

    def update(self, evaluatedIndividuals):
        self.individuals = sorted(self.individuals + evaluatedIndividuals, key=lambda x: x.fitnessValue)[0:populationSize]