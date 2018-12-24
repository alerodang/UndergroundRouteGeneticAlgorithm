import random

class RouteGenerator:

    def __init__(self, dataReader):
        self.__dataReader = dataReader
        self.__journeysDictionary = self.__generateJourneyDictionary()

    def generateRouteBetween(self, origin, destiny):

        route = [origin]

        while True:
            possibleNextStations = list(self.__journeysDictionary[route[-1]].keys())
            route.append(random.choice(possibleNextStations))
            if route[-1] == destiny:
                return route

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
