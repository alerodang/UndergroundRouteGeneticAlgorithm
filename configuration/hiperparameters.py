from enum import Enum
#DO NOT TOUCH THIS PARAMETERS AT LEAST YOU KNOW WHAT ARE YOU DOING

populationSize = 5
newParentsAmount = 2
mutationProbability = 0.4
numberOfIterations = 20

class DIRECTION(Enum):
     OUTWARD = "Outward"
     RETURN = "Return"


class ROUTE(Enum):
     ORIGIN = "Origin"
     DESTINY = "Destiny"

##################################################################