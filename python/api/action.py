#---------------------------
#everything about action data
#---------------------------
from DBConnection import DBConnection
import misc

# API method to read all actions
def read_all():
    return Action().loadAll();

# API method to add an action
def add(action):
    return Action().add(action);

# method to get an action and create if not existing
def getAction(search):
    return Action().getAction(search);
#---------------------------
#Action class handles all logic about actions
#---------------------------
class Action(object):
    
    # reads all actions from DB
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Action"].find({}))
    
    # add an new action to the DB
    def add(self, action):
        statisticDB = DBConnection.getStatisticDB()
        statisticDB["Action"].insert(action);
    
    # converts the DB result to a list of actions
    # and converts the id to string so API can serialize it
    def readCursor(self, cursor):
        actions = list()
        for action in cursor:
            misc.escapeID(action)
            actions.append(action)
        return actions
    
    # converts the DB result to a list of actions
    # but keeps the id object
    # leads to serializing issues but is needed for insert
    def readCursorKeepId(self, cursor):
        actions = list()
        for action in cursor:
            actions.append(action)
        return actions
    
    # method to get an action and create if not existing
    # keeps the id for insert
    def getAction(self, search):
        statisticDB = DBConnection.getStatisticDB()
        actions = self.readCursor(statisticDB["Action"].find(search))
        if (len(actions) > 0) :
            return actions[0]
        self.add(search)
        actions = self.readCursor(statisticDB["Action"].find(search))
        return actions[0]