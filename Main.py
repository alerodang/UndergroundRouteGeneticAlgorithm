from generateRoute.IndividualsGenerator import IndividualsGenerator
from generateRoute.TransferManager import TransferManager
from geneticalAlgorithm.operators.Mutation import Mutator
from getData.DataReader import DataReader
from geneticalAlgorithm.Population import Population
from geneticalAlgorithm.operators.Selection import selection
from geneticalAlgorithm.operators.Crossover import crossover
from geneticalAlgorithm.operators.Evaluation import Evaluator


generator = IndividualsGenerator(DataReader('data/Datos_AGs_Buscardor_de_Rutas_v0.xlsx'))
population = Population(50, 64, generator)
evaluator = Evaluator(generator.journeys, TransferManager(1380))
mutator = Mutator(generator)
evaluator.evaluate(population.individuals)

def printPopulation():
    global individual, route, gen
    for individual in population.individuals:
        route = ""
        for gen in individual.chromosome:
            route += str(gen.stationId) + "[" + gen.line + "] "
        print(route, "->", individual.fitnessValue)
    print("\n")


for i in range(0, 100):
    printPopulation()
    pairs = selection(population)
    offsprings = crossover(pairs)
    mutatedIndividuals = mutator.mutate(offsprings)
    evaluator.evaluate(mutatedIndividuals)
    population.update(mutatedIndividuals)





