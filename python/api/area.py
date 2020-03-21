import DBConnection

def read_all():
    return Valve().loadAll();

class Area(object):
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return statisticDB["Area"].find({})