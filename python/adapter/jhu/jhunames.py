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

f = open('names.csv', 'w')

def doFile(file):
	df = pd.read_csv(file)
	for index, row in map_country.iterrows():
		df.loc[df['Country/Region'] == row['cases'], "Country/Region"] = row['world_bank']
	outdf = df['Country/Region']
	for n in outdf.values:
		f.write(f"{n},\n")
	#print(outdf.values)






CSVPATH= "COVID-19/csse_covid_19_data/csse_covid_19_daily_reports"


for root, dirs, files in os.walk(CSVPATH):
	for file in files:
		if os.path.splitext(file)[1] == ".csv":
			print(file)
			doFile(CSVPATH +  '/' + file)
f.close()
#doFile(CSVPATH +  '/' + '01-30-2020.csv')























