import requests

# Random email from temp-mail.org
body = {
    "email": "lipifak983@sartess.com"
}
header = {
    'Content-Type' : 'application/json'
} 

# Random Data Generator REST API produces fictional - personal data on demand.
response = requests.post("https://random.api.randomkey.io/v1/register", headers=header, json=body)

print(response.json())
