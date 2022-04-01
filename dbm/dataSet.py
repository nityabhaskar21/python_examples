import dbm

# dbm package in python provides a simple dictionary like interface of the form DBM (DataBase Manager)
# dbm stores data in simple key – value pair form like a dictionary ,
# which makes it easier to insert, edit and retrieve data from database.

# dbm.open(file, flag=’r’)
# ‘r’: open the existing database with permission to read only.
# ‘w’: open the existing database with permission to read and write.
# ‘c’: open the database for read and write, also create a new one if it doesn’t exists.
# ‘n’: Always create a new database with permission to both read and write.


# items(): This method returns the items contained in the database.
# clear(): clear all the values present in the database.
# get(key): returns the value corresponding to key given in argument.
# keys(), iterkeys(): returns an iterable list containing keys of the dictionary.
# pop(key): Deletes / pops the key, value pair corresponding to key given in argument.
# setdefault(): set a default primary key given in the argument.
# sync(): Helps to synchronize data files and on disk directory.
# update(): updates the existing key value. Just like dictionary object.
# values(): iterate through all the values present in database.
# close(): Doesn’t take any argument nor returns anything. Just closes the caller object database.

db = dbm.open('store','c')     
db['auth'] = "780179396caac4adc50161bc46abdfc2"

keys = db.keys()

# Here keys are stored in byte format
# Use decode() to convert the bytes to normal string object

print("Keys: "+ str(keys))              # str() is used just to concatenate list with str for print
if bytes('auth', 'utf-8') in keys: 
    print("Auth key stored in dbm: "+ db.get('auth').decode())
else:
    print("Failed to save the key")