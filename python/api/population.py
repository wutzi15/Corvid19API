from DBConnection import DBConnection

def read_all():
    return Population().loadAll()
def search(population):
    return Population().search(population)

class Population(object):
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Population"].find({}))
    
    def search(self, measures):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Population"].find(population))
    
    
    def readCursor(self, cursor):
        populations = list()
        for population in cursor:
            population = self.dBToApi(population)
            populations.append(population)
        return populations
    
    def dBToApi(self, population):
        if (population is None) :
            return None
        population["_id"] = str(population["_id"])
        if ("source" in population) :
            population["source"]["_id"] = str(population["source"]["_id"])
        return population