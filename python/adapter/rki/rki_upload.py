import requests
import pandas as pd
from pprint import pprint
import json
import re
from datetime import datetime
import pymongo
import csv
from dateutil.parser import parse
from tqdm import tqdm
import sys
sys.path.insert(1, '../../api')
from cases import addMany

# https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0/geoservice?orderBy=AnzahlFall&orderByAsc=false
# https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv
class DBConnection:
  USER_NAME = "root"
  PASSWORD = "challenge1757"

  @staticmethod
  def getConnection():
    return pymongo.MongoClient("mongodb://" + DBConnection.USER_NAME + ":" + DBConnection.PASSWORD + "@bene.gridpiloten.de:27017/")

  @staticmethod
  def getStatisticDB():
    return DBConnection.getConnection()["Statistic"]

conn = DBConnection()
statsdb = conn.getStatisticDB()

statsdb['cases'].delete_many({'source.name': 'JHU'})

i = 0
r = requests.get("https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_COVID19/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json")
j = r.json()["features"]
df = pd.DataFrame()
ages_re = re.compile('\d+')
#with open("RKI_COVID19.csv", "r") as file:
reader = csv.DictReader(open("RKI_COVID19.csv", "r"))
total = 0
for _ in reader:
    total += 1
reader2 = csv.DictReader(open("RKI_COVID19.csv", "r"))
casesData = []
for data in tqdm(reader2, total=total):
    #pprint(data)
    outData = {}
    #data = d['attributes']
    adm = []
    adm.append("DE")
    if int(data['\ufeffIdBundesland']) < 10:
        adm.append('0'  + str(data['\ufeffIdBundesland']))
    else:
        adm.append(str(data['\ufeffIdBundesland']))
    lk = int(data['\ufeffIdBundesland']) % 100
    if lk < 10:
        lk = '00' + str(lk)
    elif lk < 100:
        lk = '0' + str(lk)
    adm.append(lk)
    outData['adm'] = adm
    outData['sex'] = data['Geschlecht']

    matches = re.findall(ages_re,data['Altersgruppe'])
    agerange = {}
    if len(matches) == 2:
        agerange['lower'] = int(matches[0])
        agerange['upper'] = int(matches[1])
    else:
        agerange['lower'] = 0
        agerange['upper'] = 0

    outData['ageRange'] = agerange
    outData['infected'] = int(data['AnzahlFall'])
    outData['dead'] = int(data['AnzahlTodesfall'])
    #2020-03-14T00:00:00.000Z
    FMT = '%Y-%m-%dT%H:%M%S.%fZ'
    dt = parse(data['Meldedatum'])
    outData['date'] = str(int(dt.timestamp()))
    outData['source'] = "RKI"
    outData['tested'] = 0
    outData['recovered'] = 0

    #if data['IdLandkreis'] == "08325":

    r = requests.put('http://bene.gridpiloten.de:4711/api/cases', json=outData)
    if r.status_code != 204:
      print(json.dumps(outData))
      print(r.content)
    #casesData.append(outData)
    i += 1
    #print(outData)
# uploadData = {}
# uploadData["cases"] = casesData
# r = requests.put('http://bene.gridpiloten.de:4711/api/cases/many', json=uploadData)
# if r.status_code != 204:
#     print(json.dumps(uploadData))
#     print(r.content)
# addMany(uploadData)
print(f"Uploaded: {i}")






