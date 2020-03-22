'''
Created on 2020-03-22

@author: wf
'''
import unittest
import sys

sys.path.insert(1, '../jhu')
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
        Population.debug=True
        Country.fromWikiData()    
        for country in Country.countries:
            print ("%s (%9s): %30s %s" % (country.isocc,country.wikiDataId,country.name,country.pop))    

    def testPop(self):
        Population.fromWikiData()
        for pop in Population.pops:
            print ("%40s: %9s" % (pop.name,pop.size))


if __name__ == "__main__":
    unittest.main()