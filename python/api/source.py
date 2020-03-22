from DBConnection import DBConnection

def read_all():
    return Source().loadAll();
def add(source):
    return Source().add(source);
def getSource(search):
    return Source().getSource(search);

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
    
    def getSource(self, search):
        statisticDB = DBConnection.getStatisticDB()
        sources = self.readCursor(statisticDB["Source"].find(search))
        if (len(sources) > 0) :
            return sources[0]
        self.add(search)
        sources = self.readCursor(statisticDB["Source"].find(search))
        return sources[0]
    
    def readCursorKeepId(self, cursor):
        sources = list()
        for source in cursor:
            sources.append(source)
        return sources