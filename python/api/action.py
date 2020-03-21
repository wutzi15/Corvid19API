from DBConnection import DBConnection

def read_all():
    return Action().loadAll();
def add(action):
    return Action().add(action);

class Action(object):
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Action"].find({}))
    
    def add(self, action):
        statisticDB = DBConnection.getStatisticDB()
        statisticDB["Action"].insert(action);
    
    def readCursor(self, cursor):
        actions = list()
        for action in cursor:
            action["_id"] = str(action["_id"])
            actions.append(action)
        return actions