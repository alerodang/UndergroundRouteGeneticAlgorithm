class Individual:

    def __init__(self, genes, fitnessValue=0):
        self.genes = genes
        self.fitnessValue = fitnessValue

    def __eq__(self, other):
        return self.genes == other.genes

    def setGenes(self, genes):
        self.genes = genes