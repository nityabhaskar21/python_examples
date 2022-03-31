import requests

# The requests module allows you to send HTTP requests using Python.
# pip install requests


#############
# get request 
response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response)

# Response in json format
print(response.json())

# Response Status code
print(response.status_code)


#############
# get request with parameters
responseWithParam = requests.get("https://jsonplaceholder.typicode.com/users", params={"id":1})
print(responseWithParam)

# Response in json format
print(responseWithParam.json())

# Response Status code
print(responseWithParam.status_code)


#############
# get request with header
token = ""
header = {
        'Authorization': token,
        'Content-Type' : 'application/json'
    } 
responseWithHeader = requests.get(
    "https://lab1.cloudinfinit.com/service/blueprint-service/api/blueprints",
     headers=header).json()

print(responseWithHeader)