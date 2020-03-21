"""
Created on 21.03.2020

@author: Tobias Hölzer
"""

import mesures
import csv
from datetime import datetime


def handle_file(filename):
    mesures.delete_all()
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for firstRow in reader:
            break
        for row in reader:
            knot = {}
            for key, value in zip(firstRow, row):
                if (key=="date" and value):
                    value = datetime.strptime(value, '%Y-%m-%d')
                knot[key] = value
            knot["adm"] = [knot["country_iso"], knot["adm1"], knot["adm2"]]
            if (knot["date"]):
                mesures.add(knot)
                print("Added statistics from {} {} to database!".format(knot["country"], knot["date"]))
