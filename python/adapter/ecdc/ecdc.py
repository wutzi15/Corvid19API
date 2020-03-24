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

statsdb['cases'].delete_many({'source.name': 'ECDC'})


reader = csv.DictReader(open("ecdc.csv", "r"))
total = 0
for _ in reader:
    total += 1
reader2 = csv.DictReader(open("ecdc.csv", "r"))
i = 0
casesData = []
for data in tqdm(reader2, total=total):
    #pprint(data)
    outData = {}
    #data = d['attributes']
    adm = []
    adm.append(data["GeoId"])

    outData['adm'] = adm
    outData['sex'] = "NaN"

    agerange = {}

    agerange['lower'] = 0
    agerange['upper'] = 0

    outData['ageRange'] = agerange
    outData['infected'] = int(data['Cases'])
    outData['dead'] = int(data['Deaths'])
    dt = parse(data['DateRep'])
    outData['date'] = str(int(dt.timestamp()))
    outData['source'] = "ECDC"
    outData['tested'] = 0
    outData['recovered'] = 0

    #if data['IdLandkreis'] == "08325":
    #
    r = requests.put('http://bene.gridpiloten.de:4711/api/cases', json=outData)
    if r.status_code != 204:
        print(json.dumps(outData))
        print(r.content)
    # casesData.append(outData)
    i += 1
    #print(outData)
# uploadData = {}
# uploadData["cases"] = casesData
# r = requests.put('http://bene.gridpiloten.de:4711/api/cases/many', json=uploadData)
# if r.status_code != 204:
#   print(json.dumps(uploadData))
#   print(r.content)
print(f"Uploaded: {i}")






