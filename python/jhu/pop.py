'''
Created on 22.03.2020

@author: wf
'''
from qwikidata.sparql import return_sparql_query_results
from google.protobuf.internal.python_message import _AddStaticMethods

class WikiData:
    @staticmethod
    def stripId(url):
        return url.replace('http://www.wikidata.org/entity/','')

class Population:
    '''
    get population info from wikidata
    '''
    pops=[]
    debug=False
    
    @staticmethod 
    def fromWikiData():
        # Province of China
        Population.oneQFromWikiData('Q1615742')
        # German Bundesländer
        Population.oneQFromWikiData('Q1221156')
        # US provinces
        Population.oneQFromWikiData('Q35657')
        # Australian provinces
        Population.oneQFromWikiData('Q5852411')
    
    @staticmethod    
    def oneQFromWikiData(q):    
        sparql='''SELECT ?province ?provinceLabel ?pop 
WHERE 
{
  # any subject
  # which is an instance of
  # https://www.wikidata.org/wiki/Property:P31
  # German Bundesland
  # https://www.wikidata.org/wiki/Q1221156
  ?province wdt:P31 wd:'''+q+'''.
  # get the population
  # https://www.wikidata.org/wiki/Property:P1082
  ?province wdt:P1082 ?pop.
  SERVICE wikibase:label {               # ... include the labels
        bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en"
  }
}
'''
        res = return_sparql_query_results(sparql)
        for record in (res['results']['bindings']):
            Population.pops.append(Population(record))


    def __init__(self, record):
        '''
        Constructor
        '''
        if Population.debug:
            print (record)
        self.name=record['provinceLabel']['value']
        self.size=record['pop']['value']
        
class Country:
    countries=[]
    
    @staticmethod
    def fromWikiData():
        sparql='''
    SELECT ?country ?countryLabel ?isocc ?pop   WHERE {
    ?country wdt:P31 wd:Q3624078 . # sovereign state
    # get the iso country code
    # https://www.wikidata.org/wiki/Property:P297
    ?country wdt:P297 ?isocc.
    # get the population
    # https://www.wikidata.org/wiki/Property:P1082
    ?country wdt:P1082 ?pop.
    SERVICE wikibase:label {
       bd:serviceParam wikibase:language "en"
    }
}'''
        res = return_sparql_query_results(sparql)
        for record in (res['results']['bindings']):
            if Population.debug:
                print (record)
            country=Country(record)
            Country.countries.append(country)
     
    def __init__(self,record):
        self.name=record['countryLabel']['value']
        self.wikiDataId=record['country']['value']
        self.wikiDataId=WikiData.stripId(self.wikiDataId)
        self.isocc=record['isocc']['value']
        self.pop=record['pop']['value']
        pass
        
            