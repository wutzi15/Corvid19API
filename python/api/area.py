from DBConnection import DBConnection

def read_all():
    return Area().loadAll();

class Area(object):
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Area"].find({}))
    
    def readCursor(self, cursor):
        areas = list()
        for area in cursor:
            areas.append(area)
        return areas