from DBConnection import DBConnection
import action
import source

def read_all():
    return Measures().loadAll()
def add(measures):
    return Measures().add(measures)
def delete_all():
    return Measures().deleteAll()
def search(measures):
    return Measures().search(measures)

class Measures(object):
    def loadAll(self):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Mesures"].find({}))

    def deleteAll(self):
        statisticDB = DBConnection.getStatisticDB()
        statisticDB["Mesures"].drop()

    
    def search(self, measures):
        statisticDB = DBConnection.getStatisticDB()
        return self.readCursor(statisticDB["Mesures"].find(measures))
    
    def add(self, measures):
        statisticDB = DBConnection.getStatisticDB()
        statisticDB["Mesures"].insert(self.apiToDB(measures))
    
    def readCursor(self, cursor):
        mesuresList = list()
        for measures in cursor:
            measures = self.dBToApi(measures)
            mesuresList.append(measures)
        return mesuresList
    
    def apiToDB(self, apiMesuer):
        mesureDB = dict()
        dbId = apiMesuer.get("_id", None)
        if (not (dbId is None )) :
            mesureDB["_id"] = dbId
            
        if ("date" in apiMesuer) :
            if not isinstance(apiMesuer["date"], datetime.datetime):
                try:
                    apiMesuer["date"] = datetime.datetime.fromtimestamp(int(apiMesuer["date"]))
                except :
                    try:
                        apiMesuer["date"] = datetime.datetime.strptime(apiMesuer["date"], '%Y-%m-%d')
                    except :
                        pass
                    #was not a timestamp
                    pass
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
     
    def dBToApi(self, dbMesures):
        if (dbMesures is None) :
            return None
        apiMesuer = dict()
        apiMesuer["_id"] = str(dbMesures["_id"])
        apiMesuer["date"] = dbMesures["date"]
        apiMesuer["adm"] = dbMesures["adm"]
        apiMesuer["source"] = dbMesures["source"]["url"]
        apiMesuer["actions"] = dbMesures["actions"]
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