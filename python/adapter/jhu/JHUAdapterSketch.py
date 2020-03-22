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


map_country = pd.read_csv("country_mapping.csv", sep=";")

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


    data['date'] = date.timestamp()
    data['dead'] = row['Deaths']
    data['infected'] = row['Confirmed']
    data['recovered'] = row['Recovered']
    data['source'] = 'JHUTest'
    adm = []
    adm.append(row['Country/Region'])
    adm.append(row['Province/State'])
    data['adm'] = adm
    agerange = {}
    agerange['lower'] = 0
    agerange['upper'] = 0
    data['ageRange'] = agerange

    data['sex'] = 'NaN'
    data['tested'] = 0
    print(json.dumps(data))
    r = requests.put('http://bene.gridpiloten.de:4711/api/cases', json = data)

conn = DBConnection()
statsdb = conn.getStatisticDB()

CSVPATH= "COVID-19/csse_covid_19_data/csse_covid_19_daily_reports"

statsdb['cases'].delete_many({'source.name': 'JHUTest'})

for root, dirs, files in os.walk(CSVPATH):
    for file in files:
        if os.path.splitext(file)[1] == ".csv":
            print(file)
            doFile(CSVPATH +  '/' + file)

#doFile(CSVPATH +  '/' + '01-30-2020.csv')





