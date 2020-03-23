#---------------------------
# miscellaneous stuff everywhere used
#---------------------------
import datetime

# converts teh MongoDB id to be serializable
def escapeID(data):
    data["_id"] = str(data["_id"])
    
# converts a incoming date to a datetime object
def toDateTime(data, field):
    if (field in data) :
        if not isinstance(data[field], datetime.datetime):
            try:
                #try timestamp
                data[field] = datetime.datetime.fromtimestamp(int(data[field]))
            except :
                try:
                    #try date string
                    apiMesuer["date"] = datetime.datetime.strptime(apiMesuer["date"], '%Y-%m-%d')
                except :
                    pass