"""
Created on 21.03.2020

@author: Tobias Hölzer
"""

import csv

action_names = [
    "border_control",
    "home_office",
    "closure_leisureandbars",
    "shutdown_publictransport",
    "closure_football_stadiums",
    "lockdown",
    "schools_closed",
    "traveller_quarantine",
    "primary_residence",
    "test_limitations",
    "ban_events_over_1000",
    "small_groups_only"
]
#['author'0, 'country'1, 'state'2, 'city_or_region'3, 'country_iso'4, 'adm1'5, 'adm2'6, 'date'7, 'border_control'8, 'home_office'9, 'closure_leisureandbars'10, 'shutdown_publictransport'11,
# 'closure_football_stadiums'12, 'lockdown'13, 'schools_closed'14, 'traveller_quarantine'15, 'primary_residence'16, 'test_limitations'17, 'ban_events_over_1000'18, 'misc'19, 'source'20,
# 'compliance_estimate', 'compliance_source']

indexes = {
    "date": 7,
    "country_iso": 4,
    "adm1": 5,
    "adm2": 6,
    "border_control": 8,
    "home_office": 9,
    "closure_leisureandbars": 10,
    "shutdown_publictransport": 11,
    "closure_football_stadiums": 12,
    "lockdown": 13,
    "schools_closed": 14,
    "traveller_quarantine": 15,
    "primary_residence": 16,
    "test_limitations": 17,
    "ban_events_over_1000": 18,
    "small_groups_only": -1,
    "misc": 19,
    "source": 20
}


def handle_file(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for _ in reader:
            print(_)
            break
        for row in reader:
            adm = [row[indexes["country_iso"]], row[indexes["adm1"]], row[indexes["adm2"]]]
            date = row[indexes["date"]]
            actions = [row[indexes[action]] for action in action_names]
            misc = row[indexes["misc"]]
            source = row[indexes["source"]]
            knot = MeassuresKnot(date, adm, actions, misc, source)
            knot.print()


class MeassuresKnot:

    def __init__(self, date, adm, actions, misc, source):
        self.date = date
        self.adm = adm
        self.actions = actions
        self.misc = misc
        self.source = source

    def print(self):
        print(self.__dict__)

handle_file("meassuredata.csv")
