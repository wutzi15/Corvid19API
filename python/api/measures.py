#---------------------------
# everything about measures data
# measures containing information about events causing social distancing 
#---------------------------
from DBConnection import DBConnection
import action
import source
import misc

# API method to read all measures
def read_all():
    return Measures().loadAll()

# API method to add a measures
def add(measures):
    return Measures().add(measures)

# API method to delete measures
# ! handle with care !
def delete_all():
    return Measures().deleteAll()

# API method receive measures by a filter request
def search(measures):
    return Measures().search(measures)

#---------------------------
# Measures class handles all logic about measures
#---------------------------
class Measures(object):
    
    # reads all measures from DB
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Mesures"].find({}))

    # method to delete measures
    # ! handle with care !
    def deleteAll(self):
        statisticDB = DBConnection.getStatisticDB()
        statisticDB["Mesures"].drop()
    
    # query filtered measures from DB
    def search(self, measures):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Mesures"].find(measures))
    
    # add a new measures to the DB
    def add(self, measures):
        statisticDB = DBConnection.getStatisticDB()
        statisticDB["Mesures"].insert(self.apiToDB(measures))
    
    # converts the DB result to a list of cases
    def readCursor(self, cursor):
        mesuresList = list()
        for measures in cursor:
            measures = self.dBToApi(measures)
            mesuresList.append(measures)
        return mesuresList
    
    # cleans and converts the received data for the DB
    def apiToDB(self, apiMesuer):
        mesureDB = dict()
        if ("_id" in apiMesuer) :
            mesureDB["_id"] = apiMesuer["_id"]
        misc.toDateTime(apiMesuer, "date")
        mesureDB["date"] = apiMesuer["date"]
        mesureDB["adm"] = apiMesuer["adm"]
        mesureDB["source"] = source.getSource({"url": apiMesuer["source"]})
        mesureDB["actions"] = list()
        if (apiMesuer["border_control"] in ["TRUE", "true", "True", True]) :
            mesureDB["actions"].append(action.getAction({"name": "border_control"}))
        if (apiMesuer["home_office"] in ["TRUE", "true", "True", True]) :
            mesureDB["actions"].append(action.getAction({"name": "home_office"}))
        if (apiMesuer["closure_leisureandbars"] in ["TRUE", "true", "True", True]) :
            mesureDB["actions"].append(action.getAction({"name": "closure_leisureandbars"}))
        if (apiMesuer["lockdown"] in ["TRUE", "true", "True", True]) :
            mesureDB["actions"].append(action.getAction({"name": "lockdown"}))
        if (apiMesuer["schools_closed"] in ["TRUE", "true", "True", True]) :
            mesureDB["actions"].append(action.getAction({"name": "schools_closed"}))
        if (apiMesuer["traveller_quarantine"] in ["TRUE", "true", "True", True]) :
            mesureDB["actions"].append(action.getAction({"name": "traveller_quarantine"}))
        if (apiMesuer["primary_residence"] in ["TRUE", "true", "True", True]) :
            mesureDB["actions"].append(action.getAction({"name": "primary_residence"}))
        if (apiMesuer["test_limitations"] in ["TRUE", "true", "True", True]) :
            mesureDB["actions"].append(action.getAction({"name": "test_limitations"}))
        return mesureDB
     
    # converts the DB result for the API to be serializable
    def dBToApi(self, dbMesures):
        if (dbMesures is None) :
            return None
        apiMesuer = dict()
        misc.escapeID(dbMesures)
        apiMesuer["_id"] =dbMesures["_id"]
        misc.toDateTime(dbMesures, "date")
        apiMesuer["date"] = dbMesures["date"]
        apiMesuer["adm"] = dbMesures["adm"]
        if ("source" in dbMesures) :
            misc.escapeID(dbMesures["source"])
            apiMesuer["sourceFull"] = dbMesures["source"]
            apiMesuer["source"] = dbMesures["source"]["url"]
        apiMesuer["actions"] = list()
        for action in dbMesures["actions"]:
            misc.escapeID(action)
            apiMesuer["actions"].append(action)
            if (action["name"] == "border_control") :
                apiMesuer["border_control"] = True
            if (action["name"] == "home_office") :
                apiMesuer["home_office"] = True
            if (action["name"] == "closure_leisureandbars") :
                apiMesuer["closure_leisureandbars"] = True
            if (action["name"] == "lockdown") :
                apiMesuer["lockdown"] = True
            if (action["name"] == "schools_closed") :
                apiMesuer["schools_closed"] = True
            if (action["name"] == "traveller_quarantine") :
                apiMesuer["traveller_quarantine"] = True
            if (action["name"] == "primary_residence") :
                apiMesuer["primary_residence"] = True
            if (action["name"] == "test_limitations") :
                apiMesuer["test_limitations"] = True
        return apiMesuer