class Individual:

    def __init__(self, genes, fitnessValue):
        self.genes = genes
        self.fitnessValue = fitnessValue

    def __eq__(self, other):
        return self.genes == other.genes
