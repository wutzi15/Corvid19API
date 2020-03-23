#---------------------------
# handles transparent the connection to the MongoDB
#---------------------------
import pymongo

class DBConnection:
  USER_NAME = "root"
  PASSWORD = "challenge1757"
  
  # returns the connection to the DB server
  @staticmethod
  def getConnection():
    return pymongo.MongoClient("mongodb://" + DBConnection.USER_NAME + ":" + DBConnection.PASSWORD + "@bene.gridpiloten.de:27017/")
  
  # returns the connection the live database
  @staticmethod  
  def getStatisticDB():
    return DBConnection.getConnection()["Statistic"]
