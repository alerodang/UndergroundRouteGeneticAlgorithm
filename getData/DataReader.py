import pandas as pd


class DataReader:

    def __init__(self, dataPath):
        self.dataPath = dataPath

    def getJourneys(self):
        excelFile = pd.ExcelFile(self.dataPath)
        journeys = pd.read_excel(excelFile, 'Arcos Trayectos')
        journeys = journeys.iloc[1:journeys.shape[0], 1:4]
        journeys.columns = ['Origin', 'Destiny', 'Duration']
        return journeys

