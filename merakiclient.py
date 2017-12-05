import requests
import settings

url = "https://dashboard.meraki.com/api/v0/devices/Q2HD-7EGG-YVUQ/clients"

querystring = {"timespan":"720"}

API = settings.api

headers = {
    'x-cisco-meraki-api-key': API,
    'cache-control': "no-cache",
    'postman-token': "a48c2e40-b477-5a46-fe55-24a9877c5134"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
