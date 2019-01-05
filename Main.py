from generateRoute.IndividualsGenerator import IndividualsGenerator
from getData.DataReader import DataReader
from geneticalAlgorithm.Population import Population
from geneticalAlgorithm.operators.Selection import selection
from geneticalAlgorithm.operators.Crossover import crossover

generator = IndividualsGenerator(DataReader('data/Datos_AGs_Buscardor_de_Rutas_v0.xlsx'))
population = Population(44, 52, generator)

pairs = selection(population)
offsprings = crossover(pairs)

