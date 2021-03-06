import pandas as pd
from configuration.hiperparameters import ROUTE


class DataReader:

    def __init__(self, dataPath):
        self.dataPath = dataPath

    def getJourneys(self):
        excelFile = pd.ExcelFile(self.dataPath)
        journeys = pd.read_excel(excelFile, 'Arcos Trayectos')
        journeys = journeys.iloc[1:journeys.shape[0], 1:4]
        journeys.columns = [ROUTE.ORIGIN.value, ROUTE.DESTINY.value, 'Duration']
        return journeys

    def getLines(self):
        excelFile = pd.ExcelFile(self.dataPath)
        lines = pd.read_excel(excelFile, 'Líneas y Trayectos Líneas', header=None)
        lines = lines.iloc[0:lines.shape[0], 0:12]
        return lines

    def getTimeTables(self):
        excelFile = pd.ExcelFile(self.dataPath)
        timeTables = pd.read_excel(excelFile, 'Horarios Líneas')
        return timeTables