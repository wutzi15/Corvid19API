from DBConnection import DBConnection

def read_all():
    return Mesures().loadAll();
def add(mesures):
    return Mesures().add(mesures);

class Mesures(object):
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Mesures"].find({}))
    
    def add(self, source):
        statisticDB = DBConnection.getStatisticDB()
        statisticDB["Mesures"].insert(mesures);
    
    def readCursor(self, cursor):
        mesuresList = list()
        for mesures in cursor:
            mesures["_id"] = str(mesures["_id"])
            mesuresList.append(mesures)
        return mesuresList