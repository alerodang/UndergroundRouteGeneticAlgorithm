from generateRoute.RouteGenerator import RouteGenerator
from getData.DataReader import DataReader

dataReader = DataReader('data/Datos_AGs_Buscardor_de_Rutas_v0.xlsx')

routeGenerator = RouteGenerator(dataReader)
route = routeGenerator.generateRouteBetween(224, 223)
print(route)
