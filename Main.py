from generateRoute.IndividualsGenerator import IndividualsGenerator
from generateRoute.TransferManager import TransferManager
from geneticalAlgorithm.operators.Mutation import Mutator
from getData.DataReader import DataReader
from geneticalAlgorithm.Population import Population
from geneticalAlgorithm.operators.Selection import selection
from geneticalAlgorithm.operators.Crossover import crossover
from geneticalAlgorithm.operators.Evaluation import Evaluator
from configuration.initialConfiguration import originStationId, destinyStationId, initialHour, initialMinute
from configuration.hiperparameters import numberOfIterations


generator = IndividualsGenerator(DataReader('data/Datos_AGs_Buscardor_de_Rutas_v0.xlsx'))
population = Population(originStationId, destinyStationId, generator)
evaluator = Evaluator(generator.journeys, TransferManager((initialHour * 60 + initialMinute) % 24))
mutator = Mutator(generator)
evaluator.evaluate(population.individuals)

def printPopulation(index):
    global individual, route, gen
    print("GENERACIÓN", index + 1)
    for individual in population.individuals:
        route = ""
        for gen in individual.chromosome:
            route += str(gen.stationId) + "[" + gen.line + "] "
        print(route, "-> fitnessValue:", individual.fitnessValue)
    print("\n")


for i in range(0, numberOfIterations):
    printPopulation(i)
    pairs = selection(population)
    offsprings = crossover(pairs)
    mutatedIndividuals = mutator.mutate(offsprings)
    evaluator.evaluate(mutatedIndividuals)
    population.update(mutatedIndividuals)

print("La mejor ruta encontrada entre", originStationId, "y", destinyStationId, "es:")
bestIndividual = sorted(population.individuals, key=lambda x: x.fitnessValue, reverse=True)[0]
for gen in bestIndividual.chromosome:
    route += str(gen.stationId) + "[" + gen.line + "] "
print(route, "->", bestIndividual.fitnessValue)


