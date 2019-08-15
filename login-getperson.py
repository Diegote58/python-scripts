#!/usr/bin/python
import time
import requests
import json
login = 'http://localhost:8080/token/login'
print (login)
headers = {'Content-type': 'application/json'}
payload = {'userName': '1M', 'password': '1234'}
response = requests.post(login, json=payload, headers=headers)
# parse x:
y = json.loads(response.text)
# the result is a Python dictionary:
token = "Bearer %s" % y[0]['authToken']['token']
print("operatorId: %s" % y[0]['authToken']['claims']['sub'])
print ("------------------------------------------")

getPerson = 'http://localhost:8080/secure/person/1'
print (getPerson)
headers = {'Content-type': 'application/json', 'X-Authorization': token}
response = requests.get(getPerson, headers=headers)
# parse x:
y = json.loads(response.text)
# the result is a Python dictionary:
print("personId: %s" % y['id'])
print ("------------------------------------------")
