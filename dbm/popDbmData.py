import dbm

# ‘w’: open the existing database with permission to read and write.
db = dbm.open('store','w')   

print("Before pop: "+ str(db.keys()))

db.pop('auth')

print("After pop: "+ str(db.keys()))