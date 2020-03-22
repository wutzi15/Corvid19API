import requests
import pandas as pd
from pprint import pprint
import json
import re
from datetime import datetime
import pymongo


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


r = requests.get("https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_COVID19/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json")
j = r.json()["features"]
df = pd.DataFrame()
ages_re = re.compile('\d+')
for d in j:
    outData = {}
    data = d['attributes']
    adm = []
    adm.append("DE")
    if data['IdBundesland'] < 10:
        adm.append('0'  + str(data['IdBundesland']))
    else:
        adm.append(str(data['IdBundesland']))
    lk = int(data['IdBundesland']) % 100
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
    outData['infected'] = data['AnzahlFall']
    outData['dead'] = data['AnzahlTodesfall']
    dt = datetime.fromtimestamp(data['Meldedatum'] / 1000)
    outData['date'] = f"{dt:%Y-%m-%d}"
    outData['source'] = "RKI"
    outData['tested'] = 0
    outData['recovered'] = 0
    #json.dumps(outData)
    r = requests.put('http://bene.gridpiloten.de:4711/api/cases', json = outData)
    print(outData)







