import requests

# Random email from temp-mail.org
body = {
    "email": "lipifak983@sartess.com"
}
header = {
    'Content-Type' : 'application/json'
} 
response = requests.post("https://random.api.randomkey.io/v1/register", headers=header, json=body)

print(response.json())
