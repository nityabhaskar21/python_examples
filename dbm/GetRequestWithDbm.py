import requests
import dbm

# Here we are using 'w' flag 
# ‘w’: open the existing database with permission to read and write.
# ‘c’: open the database for read and write, also create a new one if it doesn’t exists.

db = dbm.open('store','w')   
keys = db.keys()
if bytes('auth', 'utf-8') in keys: 
    header = {
    'auth': db.get('auth').decode(),
    'Content-Type' : 'application/json'
    }
    
    # Random Data Generator REST API produces fictional - personal data on demand.
    response = requests.get("https://random.api.randomkey.io/v1/quota", headers=header)
    print(response.json())
else:
    print("Failed to find the key")
