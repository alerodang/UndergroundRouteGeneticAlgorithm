import random
from configuration.hiperparameters import mutationProbability
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
        firstGen, secondGen = random.sample(individual.chromosome[1:-1], 2)
        subChromosome = self.individualsGenerator.generateChromosome(firstGen.stationId, secondGen.stationId)

        firstGenIndex = individual.chromosome.index(firstGen)
        secondGenIndex = individual.chromosome.index(secondGen)

        chromosome = individual.chromosome[0:firstGenIndex] + subChromosome + individual.chromosome[secondGenIndex + 1:]
        individual.setChromosome(repairChromosome(chromosome))
