import random

from geneticalAlgorithm.Individual import Individual


def crossover(pairs):

    offspring = []

    for pair in pairs:
        firstParent = pair[0]
        secondParent = pair[1]
        possibleRecombineGenes = list(set(firstParent.genes[1:-1]).intersection(secondParent.genes[1:-1]))
        if len(possibleRecombineGenes) == 0:
            continue

        recombineGen = random.choice(possibleRecombineGenes)

        firstParentIndex = firstParent.genes.index(recombineGen)
        secondParentIndex = secondParent.genes.index(recombineGen)

        offspring.append(repairChromosome(firstParent.genes[0:firstParentIndex] + secondParent.genes[secondParentIndex:]))
        offspring.append(repairChromosome(secondParent.genes[0:secondParentIndex] + firstParent.genes[firstParentIndex:]))

    return list(map(lambda x: Individual(x), offspring))

def repairChromosome(chromosome):

    firstRepeatedAllele = -1
    for allele in chromosome:
        if chromosome.count(allele) > 1:
            firstRepeatedAllele = allele
            break

    if firstRepeatedAllele == -1:
        return chromosome

    firstRepeatedAlleleIndex = chromosome.index(firstRepeatedAllele)
    secondRepeatedAlleleIndex = chromosome[firstRepeatedAlleleIndex + 1:].index(firstRepeatedAllele)

    return chromosome[0:firstRepeatedAlleleIndex] + chromosome[firstRepeatedAlleleIndex + 1 + secondRepeatedAlleleIndex:]
