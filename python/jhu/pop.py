'''
Created on 22.03.2020

@author: wf
'''
from qwikidata.sparql import return_sparql_query_results

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
        