import pymongo

class DBConnection:
  USER_NAME = "root"
  PASSWORD = "challenge1757"
  
  @staticmethod
  def getConnection():
    return pymongo.MongoClient("mongodb://" + USER_NAME + ":" + PASSWORD + "@bene.gridpiloten.de:27017/")
  
  @staticmethod  
  def getStatisticDB():
    return getConnection()["Statistic"]
