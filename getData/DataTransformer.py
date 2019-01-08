def generateJourneyDictionary(dataReader):
    journeysDictionary = {}

    for _, row in dataReader.getJourneys().iterrows():
        __update(journeysDictionary, row, 'Origin', 'Destiny')
        __update(journeysDictionary, row, 'Destiny', 'Origin')

    return journeysDictionary


def __update(journeysDictionary, row, origin, destiny):
    if row[origin] not in journeysDictionary.keys():
        journeysDictionary[row[origin]] = {row[destiny]: row['Duration']}
    else:
        journeysDictionary[row[origin]].update({row[destiny]: row['Duration']})


def generateLinesDictionary(dataReader):

    linesDictionary = {}

    for _, row in dataReader.getLines().iterrows():
        if row[0] not in linesDictionary.keys():
            linesDictionary[row[0]] = {"Outward": list(row[1:])}
            line = list(row[1:])
            line.reverse()
            linesDictionary[row[0]].update({"Return": line})

    return linesDictionary