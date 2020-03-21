from DBConnection import DBConnection

def read_all():
    return Source().loadAll();
def add(source):
    return Source().add(source);

class Source(object):
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Source"].find({}))
    
    def add(self, source):
        statisticDB = DBConnection.getStatisticDB()
        statisticDB["Source"].insert(source);
    
    def readCursor(self, cursor):
        sources = list()
        for source in cursor:
            source["_id"] = str(source["_id"])
            sources.append(source)
        return sources