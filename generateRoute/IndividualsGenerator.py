import random

from geneticalAlgorithm.Individual import Individual


class IndividualsGenerator:

    def __init__(self, dataReader):
        self.__dataReader = dataReader
        self.__journeys = self.__generateJourneyDictionary()
        self.__visitedStations = []

    def generateIndividual(self, origin, destiny):
        route = self.generateRoute(origin, destiny)
        return Individual(route)

    def getJourneys(self):
        return self.__journeys

    def generateRoute(self, currentStation, destiny):

        self.__visitedStations.append(currentStation)

        if currentStation == destiny:
            self.__visitedStations = []
            return [currentStation]

        nextStations = self.__expand(currentStation)

        while nextStations:
            station = random.choice(nextStations)
            nextStations.remove(station)

            if station in self.__visitedStations:
                continue

            newRoute = self.generateRoute(station, destiny)

            if newRoute:
                return [currentStation] + newRoute

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

