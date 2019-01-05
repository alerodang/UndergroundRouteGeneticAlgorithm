import random
from parameters import newParentsAmount


def selection(population):
    selection = __tournamentSelection(population)
    selection1 = __tournamentSelection(population)
    pairs = zip(selection, selection1)
    return pairs


def __selectKParents(population):
    selection = []

    fitnessValueSum = 0
    for individual in population.individuals:
        fitnessValueSum += individual.fitnessValue

    while len(selection) < newParentsAmount:

        randomValue = random.uniform(0, fitnessValueSum)

        for i in range(0, len(population.individuals)):
            randomValue -= population.individuals[i].fitnessValue
            if randomValue < 0:
                selection.append(population.individuals[i])
                break

    return selection


def __tournamentSelection(population):

    selection = []

    while len(selection) < newParentsAmount:
        selection.append(min(random.sample(population.individuals, 3), key=lambda x: x.fitnessValue))

    return selection