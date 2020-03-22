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
    try:
        popDb["Time"] = datetime.datetime.strptime(pops["Time"], '%Y')
    except:
        popDb["Time"] = "NaN"
    try:
        popDb["MidPeriod"] = float(pops["MidPeriod"])
    except:
        popDb["MidPeriod"] = "NaN"
    try:
        agestart = int(pops["AgeGrpStart"])
        ageSpan = int(pops["AgeGrpSpan"])
        ageEnd = agestart + ageSpan -1
        popDb["ageRange"] = {"lower": agestart, "upper": ageEnd}
    except:
        popDb["ageRange"] = "NaN"
    try:
        popDb["PopMale"] = int(pops["PopMale"].replace('.', ''))
    except:
        popDb["PopMale"] = "NaN"
    try:
        popDb["PopFemale"] = int(pops["PopFemale"].replace('.', ''))
    except:
        popDb["PopFemale"] = "NaN"
    try:
        popDb["PopTotal"] = int(pops["PopTotal"].replace('.', ''))
    except:
        popDb["PopTotal"] = "NaN"
    popDb["PopDensity"] = "NaN"
    popDb["source"] = dataSource
    statistic["Population"].insert(popDb)
    

dataSource = source.getSource({"name": "UN TotalPopulationBySex"})
rawDB = connection["raw"]
statistic = DBConnection.getStatisticDB();
popDatas = rawDB["unitedNations_TotalPopulationBySex"].find({})
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
    try:
        popDb["Time"] = datetime.datetime.strptime(pops["Time"], '%Y')
    except:
        popDb["Time"] = "NaN"
    try:
        popDb["MidPeriod"] = float(pops["MidPeriod"])
    except:
        popDb["MidPeriod"] = "NaN"
    popDb["ageRange"] = "NaN"
    try:
        popDb["PopMale"] = int(pops["PopMale"].replace('.', ''))
    except:
        popDb["PopMale"] = "NaN"
    try:
        popDb["PopFemale"] = int(pops["PopFemale"].replace('.', ''))
    except:
        popDb["PopFemale"] = "NaN"
    try:
        popDb["PopTotal"] = int(pops["PopTotal"].replace('.', ''))
    except:
        popDb["PopTotal"] = "NaN"
    try:
        popDb["PopDensity"] = int(pops["PopDensity"].replace('.', ''))
    except:
        popDb["PopDensity"] = "NaN"
    popDb["source"] = dataSource
    statistic["Population"].insert(popDb)
