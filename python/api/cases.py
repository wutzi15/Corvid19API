#---------------------------
#everything about cases data
#---------------------------
from DBConnection import DBConnection
import source
import misc

# API method to read all cases
def read_all():
    return Cases().loadAll();

# API method to add a cases
def add(cases):
    return Cases().add(cases);

# API method receive cases by a filter request
def search(cases):
    return Cases().search(cases);

def addMany(cases):
    return Cases().addMany(cases)

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

    def addMany(self, cases):
        statisticDB = DBConnection.getStatisticDB()
        casesToInsert = []
        for case in cases['cases']:
            casesToInsert.append(self.apiToDB(case))
        statisticDB["cases"].insert_many(casesToInsert)

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
        misc.toDateTime(cases, "date")
        return cases

    # converts the DB result for the API to be serializable
    def dBToApi(self, cases):
        if (cases is None) :
            return None
        misc.escapeID(cases)
        if ("source" in cases) :
            cases["sourceFull"] = cases["source"]
            cases["source"] = cases["source"]["name"]
            cases["sourceFull"]["_id"] = str(cases["sourceFull"]["_id"])
        misc.toDateTime(cases, "date")
        return cases