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
            if row['Origin'] not in journeysDictionary.keys():
                journeysDictionary[row['Origin']] = {row['Destiny']: row['Duration']}
            else:
                journeysDictionary[row['Origin']].update({row['Destiny']: row['Duration']})

        return journeysDictionary
