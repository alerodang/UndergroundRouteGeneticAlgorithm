import random
from parameters import mutationProbability
from geneticalAlgorithm.operators.Crossover import repairChromosome


class Mutator:

    def __init__(self, individualsGenerator):
        self.individualsGenerator = individualsGenerator

    def mutate(self, individuals):

        mutatedIndividuals = []

        for individual in individuals:
            mutatedIndividuals.append(individual)
            if random.uniform(0, 1) <= mutationProbability:
                self.__mutateIndividual(individual)

        return mutatedIndividuals

    def __mutateIndividual(self, individual):
        firstStation, secondStation = random.sample(individual.genes[1:-1], 2)
        subroute = self.individualsGenerator.generateChromosome(firstStation, secondStation)

        firstStationIndex = individual.genes.index(firstStation)
        secondStationIndex = individual.genes.index(secondStation)

        route = individual.genes[0:firstStationIndex] + subroute + individual.genes[secondStationIndex + 1:]
        individual.setGenes(repairChromosome(route))

