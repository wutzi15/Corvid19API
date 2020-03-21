from DBConnection import DBConnection
import action
import source

def read_all():
    return Mesures().loadAll();
def add(mesures):
    return Mesures().add(mesures);

class Mesures(object):
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Mesures"].find({}))
    
    def add(self, mesures):
        statisticDB = DBConnection.getStatisticDB()
        statisticDB["Mesures"].insert(self.apiToDB(mesures));
    
    def readCursor(self, cursor):
        mesuresList = list()
        for mesures in cursor:
            mesures = self.dBToApi(mesures)
            mesuresList.append(mesures)
        return mesuresList
    
    def apiToDB(self, apiMesuer):
        mesureDB = dict()
        dbId = apiMesuer.get("_id", None);
        if (not (dbId is None )) :
            mesureDB["_id"] = dbId
        mesureDB["date"] = apiMesuer["date"]
        mesureDB["adm"] = apiMesuer["adm"]
        mesureDB["source"] = source.getSource({"url": apiMesuer["source"]})
        mesureDB["actions"] = list()
        if (apiMesuer["border_control"]) :
            mesureDB["actions"].append(action.getAction({"name": "border_control"}))
        if (apiMesuer["home_office"]) :
            mesureDB["actions"].append(action.getAction({"name": "home_office"}))
        if (apiMesuer["closure_leisureandbars"]) :
            mesureDB["actions"].append(action.getAction({"name": "closure_leisureandbars"}))
        if (apiMesuer["lockdown"]) :
            mesureDB["actions"].append(action.getAction({"name": "lockdown"}))
        if (apiMesuer["schools_closed"]) :
            mesureDB["actions"].append(action.getAction({"name": "schools_closed"}))
        if (apiMesuer["traveller_quarantine"]) :
            mesureDB["actions"].append(action.getAction({"name": "traveller_quarantine"}))
        if (apiMesuer["primary_residence"]) :
            mesureDB["actions"].append(action.getAction({"name": "primary_residence"}))
        if (apiMesuer["test_limitations"]) :
            mesureDB["actions"].append(action.getAction({"name": "test_limitations"}))
        return mesureDB
     
    def dBToApi(self, dbMesures):
        if (dbMesures is None) :
            return None
        print(dbMesures)
        apiMesuer = dict()
        apiMesuer["_id"] = str(dbMesures["_id"])
        apiMesuer["date"] = dbMesures["date"]
        apiMesuer["adm"] = dbMesures["adm"]
        apiMesuer["source"] = dbMesures["source"]["url"]
        for action in dbMesures["actions"]:
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