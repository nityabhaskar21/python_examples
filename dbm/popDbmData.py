import dbm


db = dbm.open('store','w')   

print("Before pop: "+ str(db.keys()))

db.pop('auth')

print("After pop: "+ str(db.keys()))