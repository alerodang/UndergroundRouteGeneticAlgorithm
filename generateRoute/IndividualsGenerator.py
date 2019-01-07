import random

from generateRoute.Gen import Gen
from geneticalAlgorithm.Individual import Individual


class IndividualsGenerator:

    def __init__(self, dataReader):
        self.__dataReader = dataReader
        self.__journeys = self.__generateJourneyDictionary()
        self.__visitedStations = []
        self.lines = self.__generateLinesDictionary()

    def getJourneys(self):
        return self.__journeys

    def generateIndividual(self, originId, destinyId):
        individual = Individual(self.generateChromosome(originId, destinyId))
        #individual.chromosome[-1].line = self.__selectRandomLine(individual.chromosome[-2].stationId, individual.chromosome[-1].stationId)
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
        [nexStations.append(station) for station in self.__journeys[origin].keys()]
        return nexStations

    def __generateJourneyDictionary(self):

        journeysDictionary = {}

        for _, row in self.__dataReader.getJourneys().iterrows():

            self.__update(journeysDictionary, row, 'Origin', 'Destiny')
            self.__update(journeysDictionary, row, 'Destiny', 'Origin')

        return journeysDictionary

    def __update(self, journeysDictionary, row, origin, destiny):
        if row[origin] not in journeysDictionary.keys():
            journeysDictionary[row[origin]] = {row[destiny]: row['Duration']}
        else:
            journeysDictionary[row[origin]].update({row[destiny]: row['Duration']})

    def __generateLinesDictionary(self):

        linesDictionary = {}

        for _, row in self.__dataReader.getLines().iterrows():
            if row[0] not in linesDictionary.keys():
                linesDictionary[row[0]] = {"Outward": list(row[1:])}
                line = list(row[1:])
                line.reverse()
                linesDictionary[row[0]].update({"Return": line})

        return linesDictionary

    def __selectRandomLine(self, firstStation, secondStation):

        possibleLines = []

        for key in self.lines.keys():
            for i in range(0, len(self.lines[key]['Outward']) - 2):
                if [firstStation, secondStation] == self.lines[key]['Outward'][i:i + 2] or [firstStation, secondStation] == self.lines[key]['Return'][i:i + 2]:
                    possibleLines.append(key)
                    break

        return random.choice(possibleLines)
