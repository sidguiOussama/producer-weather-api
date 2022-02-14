import requests

def getError(data,status):
    return {"data": data , "status": status}


def getMethode(url):
    try :
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            return {"data": "Error Api" , "status" : response.status_code}
    except ValueError:
        return {"data": "Error" , "status": 400}
        
def getUrl(fileName,q,days):
    baseUrl = 'http://api.weatherapi.com/v1/'
    if fileName == 'current':
        baseUrl = baseUrl + 'current.json?' 
    elif fileName == 'forecast':
        baseUrl = baseUrl + 'forecast.json?'
    elif fileName == 'search':
        baseUrl = baseUrl + 'search.json?'
    baseUrl = baseUrl + 'key=089caf54a64843419ab95848211511'
    if q is not None : 
        baseUrl = baseUrl + '&q=' + q
    if days is not None : 
        baseUrl = baseUrl + '&days=' + days
    return baseUrl
