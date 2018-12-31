class Population:

    def __init__(self, origin, destiny, individualGenerator):
        self.__individualGenerator = individualGenerator
        self.individuals = self.generateIndividuals(origin, destiny)

    def generateIndividuals(self, origin, destiny):
        individuals = []
        while len(individuals) < 5:
            individual = self.__individualGenerator.generateIndividual(origin, destiny)
            if individual in individuals:
                continue
            individuals.append(individual)

        return individuals