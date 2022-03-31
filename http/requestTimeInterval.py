import requests
import time

index = 1

# http://www.randomnumberapi.com/
param = {
    'min': 10,
    'max': 100,
    'count': 1
}
while True:
    if index > 5:
        break
    response = requests.get("http://www.randomnumberapi.com/api/v1.0/random", params=param)
    print("Index: {0} , Response: {1}".format(index, response.json()))
    index = index + 1
    time.sleep(5)


