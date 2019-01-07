import random

from geneticalAlgorithm.Individual import Individual


def crossover(pairs):

    offspring = []

    for pair in pairs:
        firstParent = pair[0]
        secondParent = pair[1]
        possibleRecombineGenes = list(set(firstParent.chromosome[1:-1]).intersection(secondParent.chromosome[1:-1]))
        if len(possibleRecombineGenes) == 0:
            continue

        recombineGen = random.choice(possibleRecombineGenes)

        firstParentIndex = firstParent.chromosome.index(recombineGen)
        secondParentIndex = secondParent.chromosome.index(recombineGen)

        offspring.append(repairChromosome(firstParent.chromosome[0:firstParentIndex] + secondParent.chromosome[secondParentIndex:]))
        offspring.append(repairChromosome(secondParent.chromosome[0:secondParentIndex] + firstParent.chromosome[firstParentIndex:]))

    return list(map(lambda x: Individual(x), offspring))


def repairChromosome(chromosome):

    firstRepeatedAllele = None
    for gen in chromosome:
        if chromosome.count(gen) > 1:
            firstRepeatedAllele = gen
            break

    if firstRepeatedAllele is None:
        return chromosome

    firstRepeatedAlleleIndex = chromosome.index(firstRepeatedAllele)
    secondRepeatedAlleleIndex = chromosome[firstRepeatedAlleleIndex + 1:].index(firstRepeatedAllele)

    return chromosome[0:firstRepeatedAlleleIndex] + chromosome[firstRepeatedAlleleIndex + 1 + secondRepeatedAlleleIndex:]
