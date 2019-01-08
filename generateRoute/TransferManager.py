from getData.DataReader import DataReader
from getData.DataTransformer import generateJourneyDictionary, generateLinesDictionary
from configuration.hiperparameters import DIRECTION
import math


class TransferManager:

    def __init__(self, tripInitialTime):

        self.tripInitialTime = tripInitialTime
        self.__dataReader = DataReader('data/Datos_AGs_Buscardor_de_Rutas_v0.xlsx')
        self.__journeys = generateJourneyDictionary(self.__dataReader)
        self.__lines = generateLinesDictionary(self.__dataReader)
        self.__timeTable = self.__dataReader.getTimeTables()

    def calculateTimeToArrival(self, originStationId, destinyStationId, line, currentTime):

        direction = self.__calculateTrainDirection(originStationId, destinyStationId, line)
        trainTimeToStation = self.__calculateTrainTimeToStation(originStationId, line, direction)
        for time in self.__dataReader.getTimeTables()[line + " " + direction].values:

            if math.isnan(time):
                return 1440 - currentTime + self.__dataReader.getTimeTables()[line + " " + direction][0] + trainTimeToStation

            if time >= currentTime - trainTimeToStation:
                return time - currentTime + trainTimeToStation

        return 1440 - currentTime + self.__dataReader.getTimeTables()[line + " " + direction][-1] + trainTimeToStation

    def __calculateTrainTimeToStation(self, originStationId, line, direction):

        trainTimeToStation = 0

        for i in range(0, len(self.__lines[line][direction]) - 1):

            if math.isnan(self.__lines[line][direction][i]) or originStationId == self.__lines[line][direction][i]:
                break

            trainTimeToStation += self.__journeys[self.__lines[line][direction][i]][self.__lines[line][direction][i+1]]

        return trainTimeToStation

    def __calculateTrainDirection(self, originStationId, destinyStationId, line):

        for i in range(0, len(self.__lines[line][DIRECTION.OUTWARD.value]) - 2):
            if [originStationId, destinyStationId] == self.__lines[line][DIRECTION.OUTWARD.value][i:i+2]:
                return DIRECTION.OUTWARD.value

        return DIRECTION.RETURN.value


