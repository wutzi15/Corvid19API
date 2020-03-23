#---------------------------
#everything about cases data
#---------------------------
from DBConnection import DBConnection
import source
import datetime

# API method to read all cases
def read_all():
    return Cases().loadAll();

# API method to add a cases
def add(cases):
    return Cases().add(cases);

# API method receive cases by a filter request
def search(cases):
    return Cases().search(cases);

#---------------------------
# Cases class handles all logic about cases
#---------------------------
class Cases(object):
    
    # reads all cases from DB
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["cases"].find({}))
    
    # query filtered cases from DB
    def search(self, cases):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["cases"].find(cases))
    
    # add a new cases to the DB
    def add(self, cases):
        statisticDB = DBConnection.getStatisticDB()
        statisticDB["cases"].insert(self.apiToDB(cases));
    
    
    # converts the DB result to a list of cases
    def readCursor(self, cursor):
        casesList = list()
        for cases in cursor:
            casesList.append(self.dBToApi(cases))
        return casesList
    
    # cleans and converts the received data for the DB
    def apiToDB(self, cases):
        if ("source" in cases) :
            cases["source"] = source.getSource({"name": cases["source"]})
        if ("date" in cases) :
            if not isinstance(cases["date"], datetime.datetime):
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
     
     # converts the DB result for the API to be serializable
    def dBToApi(self, cases):
        if (cases is None) :
            return None
        cases["_id"] = str(cases["_id"])
        if ("source" in cases) :
            cases["sourceFull"] = cases["source"]
            cases["source"] = cases["source"]["name"]
            cases["sourceFull"]["_id"] = str(cases["sourceFull"]["_id"])
        
        if ("date" in cases) :
            if not isinstance(cases["date"], datetime.datetime):
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