from DBConnection import DBConnection

def read_all():
    return Area().loadAll();
def add(area):
    return Area().add(area);

class Area(object):
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Area"].find({}))
    
    def add(self, area):
        statisticDB = DBConnection.getStatisticDB()
        statisticDB["Area"].insert(area);
    
    def readCursor(self, cursor):
        areas = list()
        for area in cursor:
            areas.append(area)
        return areas