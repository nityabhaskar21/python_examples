#Creating dictionary
dict = {
    'Name': 'abc',
    'Age': 7,
    'Class': 'First'
    }

#Accessing 
# print("dict['Name']: ", dict['Name'])
# print("dict['Age']: ", dict['Age'])

# # Updating
# dict['Age'] = 8
# print("\nUpdated age - dict['Age']: ", str(dict['Age'])+"\n")

#Iterating
for key, value in dict.items():
     print(key, '->', value)

#Deleting
del dict['Name'];       # remove entry with key 'Name'
dict.clear();           # remove all entries in dict
del dict ;              # delete entire dictionary


