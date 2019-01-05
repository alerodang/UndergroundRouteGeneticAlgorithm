import random

from geneticalAlgorithm.Individual import Individual


class IndividualsGenerator:

    def __init__(self, dataReader):
        self.__dataReader = dataReader
        self.__journeys = self.__generateJourneyDictionary()
        self.__visitedStations = []
        self.__lines = self.__generateLinesDictionary()

    def generateIndividual(self, originId, destinyId):
        return Individual(self.generateChromosome(originId, destinyId))

    def getJourneys(self):
        return self.__journeys

    def generateChromosome(self, currentStationId, destinyId):

        self.__visitedStations.append(currentStationId)

        if currentStationId == destinyId:
            self.__visitedStations = []
            return [currentStationId]

        nextStations = self.__expand(currentStationId)

        while nextStations:
            station = random.choice(nextStations)
            nextStations.remove(station)

            if station in self.__visitedStations:
                continue

            newRoute = self.generateChromosome(station, destinyId)

            if newRoute:
                return [currentStationId] + newRoute

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

