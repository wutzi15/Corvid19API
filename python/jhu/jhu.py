
import csv
import requests
#https://stackoverflow.com/a/35371451/1497139

class TimeSeries():
    CSV_URL="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/archived_data/archived_time_series/time_series_2019-ncov-Confirmed.csv"
    
    def __init__(self):
        self.regions=[]
        with requests.Session() as s:
            download = s.get(TimeSeries.CSV_URL)

            decoded_content = download.content.decode('utf-8')

            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            regionRows = list(cr)
            for regionRow in regionRows:
                region=Region(regionRow)
                self.regions.append(region)
                
class Region():
    
    def __init__(self,row):
        self.province=row[0]
        self.country=row[1]
        
        
        
                    
