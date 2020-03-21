import pymongo

class DBConnection:
  USER_NAME = "root"
  PASSWORD = "challenge1757"
  
  @staticmethod
  def getConnection():
    return pymongo.MongoClient("mongodb://" + DBConnection.USER_NAME + ":" + DBConnection.PASSWORD + "@bene.gridpiloten.de:27017/")
  
  @staticmethod  
  def getStatisticDB():
    return DBConnection.getConnection()["jhu"]
