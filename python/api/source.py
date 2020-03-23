#---------------------------
#everything about population data
#---------------------------
from DBConnection import DBConnection
import misc

# API method to read all sources
def read_all():
    return Source().loadAll();

# API method to add a source
def add(source):
    return Source().add(source);

# method to get a source and create if not existing
def getSource(search):
    return Source().getSource(search);

#---------------------------
#Source class handles all logic about sources
#---------------------------
class Source(object):
    
    # reads all sources from DB
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Source"].find({}))
    
    # add a new sources to the DB
    def add(self, source):
        statisticDB = DBConnection.getStatisticDB()
        statisticDB["Source"].insert(source);
    
    # converts the DB result to a list of sources
    def readCursor(self, cursor):
        sources = list()
        for source in cursor:
            misc.escapeID(source)
            sources.append(source)
        return sources
    
    # method to get a source and create if not existing
    # keeps the id for insert
    def getSource(self, search):
        statisticDB = DBConnection.getStatisticDB()
        sources = self.readCursorKeepId(statisticDB["Source"].find(search))
        if (len(sources) > 0) :
            return sources[0]
        self.add(search)
        sources = self.readCursorKeepId(statisticDB["Source"].find(search))
        return sources[0]
    
    # converts the DB result to a list of sources
    # but keeps the id object
    # leads to serializing issues but is needed for insert
    def readCursorKeepId(self, cursor):
        sources = list()
        for source in cursor:
            sources.append(source)
        return sources