#!/usr/bin/python
import time
import requests
import json
import csv
from datetime import date, datetime, timedelta
dateFrom = date(1979, 7, 2)
login = 'http://localhost:8080/token/login'
print (login)
headers = {'Content-type': 'application/json'}
payload = {'userName': '1M', 'password': '1234'}
response = requests.post(login, json=payload, headers=headers)
# parse x:
jsonResponse = json.loads(response.text)
# the result is a Python dictionary:
token = "Bearer %s" % jsonResponse[0]['authToken']['token']
print("operatorId: %s" % jsonResponse[0]['authToken']['claims']['sub'])


#Funcion para recorrer valores

# Function definition is here
def getPersons():
	line_count = 0
	docNumber_count = 20000000
	docNumbers = []
	names = []
	lastnames = []
	person = []
	birth_dates = []
	sex = []
	with open('C:\\Users\\ASUS-K555U\\Downloads\\nombres-1975-1979.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')

		for row in csv_reader:
			if line_count == 0:
				#print(f'{line_count} Column names are {", ".join(row)}')
				names.append(row[0])
				docNumbers.append(str(docNumber_count))
				birth_dates.append(dateFrom - timedelta(days=line_count+3))				
				if ('a'.lower() == row[0][-1:].lower()):
					sex.append('F')
				else:
					sex.append('M')
				line_count += 1
				docNumber_count += 7
			else:
				try:
					#print(f'{line_count}-\t{row[0]}')
					names.append(row[0])
					docNumbers.append(str(docNumber_count))
					birth_dates.append(dateFrom - timedelta(days=line_count+3))
					if ('a'.lower() == row[0][-1:].lower()):
						sex.append('F')
					else:
						sex.append('M')
					line_count += 1
					docNumber_count += 5
				except:
					print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
		print(f'Processed {line_count} lines.')

	with open('C:\\Users\\ASUS-K555U\\Downloads\\apellidos_mas_frecuentes.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=';')

		for row1 in csv_reader:

			if line_count == 0:
				#print(f'{line_count} Column names are {", ".join(row1)}')
				lastnames.append(row1[1])
				line_count += 1
			else:
				try:
					#print(f'{line_count}-\t{row1[1]}')
					lastnames.append(row1[1])
					line_count += 1
				except:
					print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
		print(f'Processed {line_count} lines.')

	for name in names:
		temp = []
		temp.append(name)	
		for lastname in lastnames[:]:
			temp.append(lastname)	
			if(len(lastnames) > 1):
				lastnames.remove(lastname)
			break		
		for doc in docNumbers[:]:
			temp.append(str(doc))
			docNumbers.remove(doc)
			break
		for s in sex[:]:
			temp.append(s)
			sex.remove(s)
			break				
		for date in birth_dates[:]:
			temp.append(str(date) + ' 00:00:00')
			birth_dates.remove(date)
			break
		person.append(temp)
	return person
	
print ("------------------------------------------")

postPerson = 'http://localhost:8080/secure/person'
headers = {'Content-type': 'application/json', 'X-Authorization': token}

persons = getPersons()
#for full in persons:
	#print(full[0] + ', ' + full[1]+ ', ' + full[2]+ ', ' + full[3])

for person in persons:
	personDto = {'firstName': person[0], 'lastName': person[1],'docNumber': person[2],'sex': person[3],'birthDay': person[4]}
	response = requests.post(postPerson, headers=headers, json=personDto)
	# the result is a Python dictionary:
	print(response.status_code)
	print ("------------------------------------------")

