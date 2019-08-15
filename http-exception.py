#!/usr/bin/python
import time
import requests
from requests.exceptions import HTTPError
import json

def login(url, user, password):
	#print (url)
	headers = {'Content-type': 'application/json'}
	payload = {'userName': user, 'password': password}
	responseA = {'userName': user, 'password': password}
	try:
		response = requests.post(url, json=payload, headers=headers)
		responseA = json.loads(response.text)
		# parse x:
		jsonResponse = json.loads(response.text)
		# the result is a Python dictionary:
		token = "Bearer %s" % jsonResponse[0]['authToken']['token']
		print("operator: %s" % jsonResponse[0]['authToken']['claims']['sub'])
		# If the response was successful, no Exception will be raised
		response.raise_for_status()		
		# the result is a Python dictionary:
		#print(jsonResponse[0]['authToken'])
		print ("status : %s" % response.status_code)
	except HTTPError as http_err:
		print(f'HTTP error occurred: {http_err}')  # Python 3.6
		print("status: %s,\nmessage: %s" % (responseA['status'], responseA['message']))
	except Exception as err:
		print(f'Other error occurred: {err}')  # Python 3.6
		print("status: %s,\nmessage: %s" % (responseA['status'], responseA['message']))
	else:
		print('Success!')
		
url = 'http://localhost:8080/token/login'
for i in range(0,10):
	login(url,'1M','12345')