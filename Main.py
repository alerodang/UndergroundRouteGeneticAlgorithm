from generateRoute.IndividualsGenerator import IndividualsGenerator
from getData.DataReader import DataReader
from geneticalAlgorithm.Population import Population

generator = IndividualsGenerator(DataReader('data/Datos_AGs_Buscardor_de_Rutas_v0.xlsx'))
population = Population(44, 52, generator)
for individual in population.individuals:
    print(individual.genes)
#for i in range(0, 50):
#    print(generator.generateIndividual(44, 52).genes)

#[print(list[i], "\n") for i in range(0, 10)]
