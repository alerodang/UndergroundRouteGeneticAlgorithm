class Evaluator:

    def __init__(self, journeys, transferManager):
        self.__journeys = journeys
        self.__transferManager = transferManager

    def evaluate(self, individuals):

        for individual in individuals:
            individual.fitnessValue = self.evaluateIndividual(individual)

    def evaluateIndividual(self, individual):

        fitnessValue = 0
        currentLine = individual.chromosome[0].line

        for i in range(0, len(individual.chromosome) - 1):
            originStationId = individual.chromosome[i].stationId
            destinyStationId = individual.chromosome[i + 1].stationId
            nextLine = individual.chromosome[i + 1].line

            if currentLine != nextLine:
                currentTime = fitnessValue + self.__transferManager.tripInitialTime
                fitnessValue -= self.__transferManager.calculateTimeToArrival(originStationId,
                                                                              destinyStationId,
                                                                              nextLine,
                                                                              currentTime)

            fitnessValue -= self.__journeys[originStationId][destinyStationId]

            currentLine = nextLine

        return fitnessValue
