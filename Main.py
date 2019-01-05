from generateRoute.IndividualsGenerator import IndividualsGenerator
from geneticalAlgorithm.operators.Mutation import Mutator
from getData.DataReader import DataReader
from geneticalAlgorithm.Population import Population
from geneticalAlgorithm.operators.Selection import selection
from geneticalAlgorithm.operators.Crossover import crossover
from geneticalAlgorithm.operators.Evaluation import Evaluator


generator = IndividualsGenerator(DataReader('data/Datos_AGs_Buscardor_de_Rutas_v0.xlsx'))
population = Population(262, 332, generator)
evaluator = Evaluator(generator.getJourneys())
mutator = Mutator(generator)
evaluator.evaluate(population.individuals)

for i in range(0, 10):
    pairs = selection(population)
    offsprings = crossover(pairs)
    mutatedIndividuals = mutator.mutate(offsprings)
    evaluator.evaluate(mutatedIndividuals)
    population.update(mutatedIndividuals)


    #print(min(list(map(lambda x: x.fitnessValue, population.individuals))))
    for individual in population.individuals:
        print(individual.genes, "->", individual.fitnessValue)
    print("\n")