class Gen:

    def __init__(self, stationId, line=None):
        self.stationId = stationId
        self.line = line

    def __eq__(self, other):
        return self.stationId == other.stationId

    def __hash__(self):
        return self.stationId
