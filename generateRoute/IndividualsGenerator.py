import random

from geneticalAlgorithm.Individual import Individual


class IndividualsGenerator:

    def __init__(self, dataReader):
        self.dataReader = dataReader
        self.journeysDictionary = self.generateJourneyDictionary()
        self.visitedStations = []

    def generateIndividual(self, origin, destiny):
        route, fitnessValue = self.generateIndividualRecursively(origin, destiny)
        return Individual(route, fitnessValue)

    def generateIndividualRecursively(self, currentStation, destiny):

        self.visitedStations.append(currentStation)

        if currentStation == destiny:
            self.visitedStations = []
            return [currentStation], 0

        nextStations = self.expand(currentStation)

        while nextStations:
            station = random.choice(nextStations)
            nextStations.remove(station)

            if station in self.visitedStations:
                continue

            newRoute, fitnessValue = self.generateIndividualRecursively(station, destiny)

            if newRoute:
                return [currentStation] + newRoute, fitnessValue + self.journeysDictionary[currentStation][newRoute[0]]

        return [], 0

    def expand(self, origin):
        nexStations = []
        [nexStations.append(station) for station in self.journeysDictionary[origin].keys()]
        return nexStations

    def generateJourneyDictionary(self):

        journeysDictionary = {}

        for _, row in self.dataReader.getJourneys().iterrows():

            self.update(journeysDictionary, row, 'Origin', 'Destiny')
            self.update(journeysDictionary, row, 'Destiny', 'Origin')

        return journeysDictionary

    def update(self, journeysDictionary, row, origin, destiny):
        if row[origin] not in journeysDictionary.keys():
            journeysDictionary[row[origin]] = {row[destiny]: row['Duration']}
        else:
            journeysDictionary[row[origin]].update({row[destiny]: row['Duration']})
