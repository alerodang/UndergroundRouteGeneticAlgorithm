from getData.DataReader import DataReader


class TransferManager:

    def __init__(self, tripInitialTime):

        self.tripInitialTime = tripInitialTime
        self.__dataReader = DataReader('data/Datos_AGs_Buscardor_de_Rutas_v0.xlsx')
        self.__journeys = self.__generateJourneyDictionary()
        self.__lines = self.__generateLinesDictionary()
        self.__timeTable = self.__dataReader.getTimeTables()

    def calculateTimeToArrival(self, originStationId, destinyStationId, line, currentTime):

        direction = self.__calculateTrainDirection(originStationId, destinyStationId, line)
        trainTimeToStation = self.__calculateTrainTimeToStation(originStationId, line, direction)
        for time in self.__dataReader.getTimeTables()[line + " " + direction].values:
            if time >= currentTime - trainTimeToStation:
                return time - currentTime + trainTimeToStation

    def __calculateTrainTimeToStation(self, originStationId, line, direction):

        trainTimeToStation = 0

        for i in range(0, len(self.__lines[line][direction]) - 1):

            if originStationId == self.__lines[line][direction][i]:
                break

            trainTimeToStation += self.__journeys[self.__lines[line][direction][i]][self.__lines[line][direction][i+1]]

        return trainTimeToStation

    def __calculateTrainDirection(self, originStationId, destinyStationId, line):

        for i in range(0, len(self.__lines[line]["Outward"]) - 2):
            if [originStationId, destinyStationId] == self.__lines[line]["Outward"][i:i+2]:
                return "Outward"

        return "Return"

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


