#---------------------------
#everything about population data
#---------------------------
from DBConnection import DBConnection
import misc

# API method to read all population
def read_all():
    return Population().loadAll()

# API method receive population by a filter request
def search(population):
    return Population().search(population)

#---------------------------
# Population class handles all logic about population
#---------------------------
class Population(object):
    
    # reads all population from DB
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Population"].find({}))
    
    # query filtered population from DB
    def search(self, population):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Population"].find(population))
    
    # converts the DB result to a list of population
    def readCursor(self, cursor):
        populations = list()
        for population in cursor:
            population = self.dBToApi(population)
            populations.append(population)
        return populations
    
    # cleans and converts the received data for the DB
    def dBToApi(self, population):
        if (population is None) :
            return None
        misc.escapeID(population)
        if ("source" in population) :
            misc.escapeID(population["source"])
        return population