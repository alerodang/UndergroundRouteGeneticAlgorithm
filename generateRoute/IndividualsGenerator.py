import random

from geneticalAlgorithm.Gen import Gen
from geneticalAlgorithm.Individual import Individual
from getData.DataTransformer import generateJourneyDictionary, generateLinesDictionary
from parameters import DIRECTION


class IndividualsGenerator:

    def __init__(self, dataReader):
        self.__dataReader = dataReader
        self.journeys = generateJourneyDictionary(dataReader)
        self.__visitedStations = []
        self.lines = generateLinesDictionary(dataReader)

    def generateIndividual(self, originId, destinyId):
        individual = Individual(self.generateChromosome(originId, destinyId))
        return individual

    def generateChromosome(self, currentStationId, destinyId):

        self.__visitedStations.append(currentStationId)

        if currentStationId == destinyId:
            self.__visitedStations = []
            return [Gen(currentStationId)]

        nextStationIds = self.__expand(currentStationId)

        while nextStationIds:
            stationId = random.choice(nextStationIds)
            nextStationIds.remove(stationId)

            if stationId in self.__visitedStations:
                continue

            newRoute = self.generateChromosome(stationId, destinyId)

            if newRoute:
                route = [Gen(currentStationId, self.__selectRandomLine(currentStationId, newRoute[0].stationId))] + newRoute
                route[1].line = route[0].line
                return route

        return []

    def __expand(self, origin):
        nexStations = []
        [nexStations.append(station) for station in self.journeys[origin].keys()]
        return nexStations

    def __selectRandomLine(self, firstStation, secondStation):

        possibleLines = []

        for key in self.lines.keys():
            for i in range(0, len(self.lines[key][DIRECTION.OUTWARD.value]) - 2):
                if [firstStation, secondStation] == self.lines[key][DIRECTION.OUTWARD.value][i:i + 2] or [firstStation, secondStation] == self.lines[key][DIRECTION.RETURN.value][i:i + 2]:
                    possibleLines.append(key)
                    break

        return random.choice(possibleLines)
