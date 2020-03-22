#!/usr/bin/env python
# coding: utf-8
import os
import pandas as pd
import pymongo
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import sys
sys.path.insert(1, '../../api')
from cases import Cases
import datetime
import requests
import json
from tqdm import tqdm
import math


map_country = pd.read_csv("country_mapping.csv", sep=";")
map_jhu = pd.read_csv("jhu_mapping.csv", sep=",")

class DBConnection:
  USER_NAME = "root"
  PASSWORD = "challenge1757"

  @staticmethod
  def getConnection():
    return pymongo.MongoClient("mongodb://" + DBConnection.USER_NAME + ":" + DBConnection.PASSWORD + "@bene.gridpiloten.de:27017/")

  @staticmethod
  def getStatisticDB():
    return DBConnection.getConnection()["Statistic"]


def doFile(file):
  df = pd.read_csv(file)
  for index, row in map_country.iterrows():
    df.loc[df['Country/Region'] == row['cases'], "Country/Region"] = row['world_bank']

  for index, row in map_jhu.iterrows():
    df.loc[df['Country/Region'] == row['country'], "Country/Region"] = row['country_iso']
  i = 0
  df.fillna(0)

  for index, row in df.iterrows():
    data = {}
    date = ""
    try:
      FMT = '%Y-%m-%dT%H:%M:%S'
      date = datetime.datetime.strptime(str(row['Last Update']), FMT)
    except:
      #'1/31/2020 23:59'
      try:
        FMT = '%m/%d/%Y %H:%M'
        date = datetime.datetime.strptime(str(row['Last Update']), FMT)
      except:
        #'1/30/20 16:00'
        FMT = '%m/%d/%y %H:%M'
        date = datetime.datetime.strptime(str(row['Last Update']), FMT)


    data['date'] = str(int(date.timestamp()))
    if math.isnan(row['Deaths']):
      data['dead'] = 0
    else:
      data['dead'] = int(row['Deaths'])

    if math.isnan(row['Confirmed']):
      data['infected'] = 0
    else:
      data['infected'] = int(row['Confirmed'])
    #data['infected'] = int(row['Confirmed'])
    if math.isnan(row['Recovered']):
      data['recovered'] = 0
    else:
      data['recovered'] = int(row['Recovered'])
    #data['recovered'] = int(row['Recovered'])
    data['source'] = 'JHU'
    adm = []
    adm.append(str(row['Country/Region']))
    adm.append(str(row['Province/State']))
    data['adm'] = adm
    agerange = {}
    agerange['lower'] = 0
    agerange['upper'] = 0
    data['ageRange'] = agerange

    data['sex'] = 'NaN'
    data['tested'] = 0
    #print(json.dumps(data))
    i += 1
    r = requests.put('http://bene.gridpiloten.de:4711/api/cases', json=data)
    if r.status_code != 204:
      print(file)
      print(json.dumps(data))
      print(r.content)

  #print(f"Uploaded: {i}")
  return i

conn = DBConnection()
statsdb = conn.getStatisticDB()

CSVPATH= "COVID-19/csse_covid_19_data/csse_covid_19_daily_reports"

statsdb['cases'].delete_many({'source.name': 'JHU'})

globalI = 0

def walkdir():
  for root, dirs, files in os.walk(CSVPATH):
    for file in files:
      if os.path.splitext(file)[1] == ".csv":
        yield CSVPATH +  '/' + file

# Precomputing files count
filescount = 0
for _ in tqdm(walkdir()):
    filescount += 1


# Computing for real
for filepath in tqdm(walkdir(), total=filescount):
  globalI += doFile(filepath)

print(f"global upload: {globalI}")
#doFile(CSVPATH +  '/' + '03-17-2020.csv')



