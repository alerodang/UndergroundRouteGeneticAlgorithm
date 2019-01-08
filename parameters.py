from enum import Enum

populationSize = 5
newParentsAmount = 2
mutationProbability = 0.3


class DIRECTION(Enum):
     OUTWARD = "Outward"
     RETURN = "Return"


class ROUTE(Enum):
     ORIGIN = "Origin"
     DESTINY = "Destiny"
