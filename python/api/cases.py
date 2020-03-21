from DBConnection import DBConnection

def read_all():
    return Cases().loadAll();
def add(cases):
    return Cases().add(cases);

class Cases(object):
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["cases"].find({}))
    
    def add(self, cases):
        statisticDB = DBConnection.getStatisticDB()
        statisticDB["cases"].insert(cases);
    
    def readCursor(self, cursor):
        casesList = list()
        for cases in cursor:
            cases["_id"] = str(cases["_id"])
            casesList.append(cases)
        return casesList