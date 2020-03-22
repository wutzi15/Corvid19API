from DBConnection import DBConnection
import source
import datetime

def read_all():
    return Cases().loadAll();
def add(cases):
    return Cases().add(cases);
def search(cases):
    return Cases().search(cases);

class Cases(object):
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["cases"].find({}))
    
    def search(self, cases):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["cases"].find(cases))
    
    def add(self, cases):
        statisticDB = DBConnection.getStatisticDB()
        statisticDB["cases"].insert(self.apiToDB(cases));
    
    def readCursor(self, cursor):
        casesList = list()
        for cases in cursor:
            casesList.append(self.dBToApi(cases))
        return casesList
    
    
    def apiToDB(self, cases):
        if ("source" in cases) :
            cases["source"] = source.getSource({"name": cases["source"]})
        return cases
     
    def dBToApi(self, cases):
        if (cases is None) :
            return None
        cases["_id"] = str(cases["_id"])
        cases["source"] = cases["source"]["name"]#
        
        if ("date" in cases) :
            try:
                cases["date"] = datetime.datetime.fromtimestamp(int(cases["date"]))
            except :
                try:
                    cases["date"] = datetime.datetime.strptime(cases["date"], '%Y-%m-%d')
                except :
                    pass
                #was not a timestamp
                pass
        return cases