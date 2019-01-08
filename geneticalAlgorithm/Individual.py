class Individual:

    def __init__(self, chromosome, fitnessValue=0):
        self.chromosome = chromosome
        self.fitnessValue = fitnessValue

    def __eq__(self, other):
        return self.chromosome == other.chromosome

    def setChromosome(self, chromosome):
        self.chromosome = chromosome