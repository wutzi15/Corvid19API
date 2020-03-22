'''
Created on 2020-03-22

@author: wf
'''
import unittest
import sys

sys.path.insert(1, '../jhu')
from loc import Projection
from jhu import TimeSeries
from pop import Population, Country

debug=True

class TestJhuNames(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNames(self):
        ''' test the names from John Hopkins university time series data '''
        ts=TimeSeries()
        for region in ts.regions:
            print ("%s:%s" % (region.country,region.province))
            
    def testCountries(self):
        ''' test getting country codes and population data from wiki data '''
        Population.debug=True
        Country.fromWikiData()    
        for country in Country.countries:
            print ("%6s;%9s;%30s;9%s;%s;%s" % (country.isocc,country.wikiDataId,country.name,country.pop,country.location,country.coords))    

    def testPop(self):
        ''' test getting population data for provinces / regions from wiki data '''
        #Population.debug=True
        Population.fromWikiData()
        for pop in Population.pops:
            print ("%6s;%9s;%40s;%9s;%s;%s" % (pop.isocode,pop.wikiDataId,pop.name,pop.size,pop.location,pop.coords))

    def testProjection(self):
        point="-0.1285907, 51.50809"
        coords=Projection.pointToXy(point)
        print(coords)
        coords=Projection.wgsToXy(-0.1285907, 51.50809) # longitude first, latitude second.
        print(coords)
        

if __name__ == "__main__":
    unittest.main()