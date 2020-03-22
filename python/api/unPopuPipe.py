from DBConnection import DBConnection
import source
import pycountry
import datetime

connection = DBConnection.getConnection()
dataSource = source.getSource({"name": "UN PopulationByAgeSex_OtherVariants"})
rawDB = connection["raw"]
statistic = DBConnection.getStatisticDB();
popDatas = rawDB["unitedNation_PopulationByAgeSex_OtherVariants"].find({})
for pops in popDatas:
    popDb = dict()
    popDb["LocID"] = pops["LocID"]
    popDb["adm"] = ["","",""]
    try:
        popDb["adm"][0] = pycountry.countries.get(name=pops["Location"]).alpha_2
    except:
        popDb["adm"][0] = pops["Location"]
    popDb["VarID"] = pops["VarID"]
    popDb["Variant"] = pops["Variant"]
    popDb["Time"] = datetime.datetime.strptime(pops["Time"], '%Y')
    popDb["MidPeriod"] = float(pops["MidPeriod"])
    agestart = int(pops["AgeGrpStart"])
    ageSpan = int(pops["AgeGrpSpan"])
    ageEnd = agestart + ageSpan -1
    popDb["ageRange"] = {"lower": agestart, "upper": ageEnd}
    popDb["PopMale"] = float(pops["PopMale"])
    popDb["PopFemale"] = float(pops["PopFemale"])
    popDb["PopTotal"] = float(pops["PopTotal"])
    popDb["source"] = dataSource
    statistic["Population"].insert(popDb)