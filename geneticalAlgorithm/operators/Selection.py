import random
from configuration.hiperparameters import newParentsAmount


def selection(population):
    selection = __tournamentSelection(population)
    selection1 = __tournamentSelection(population)
    pairs = zip(selection, selection1)
    return pairs

def __tournamentSelection(population):

    selection = []

    while len(selection) < newParentsAmount:
        selection.append(max(random.sample(population.individuals, 3), key=lambda x: x.fitnessValue))

    return selection