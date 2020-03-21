from DBConnection import DBConnection

def read_all():
    return Cases().loadAll();
def add(cases):
    return Cases().add(cases);

class Cases(object):
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Cases"].find({}))
    
    def add(self, source):
        statisticDB = DBConnection.getStatisticDB()
        statisticDB["Cases"].insert(cases);
    
    def readCursor(self, cursor):
        casesList = list()
        for cases in cursor:
            cases["id"] = str(cases["_id"])
            del cases['_id']
            casesList.append(cases)
        return casesList