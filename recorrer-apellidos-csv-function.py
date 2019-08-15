import csv
import random
import threading
import numpy
from datetime import date, datetime, timedelta, time
dateFrom = date(1979, 7, 2)
line_count_g = 0
# Function definition is here
def getPersons():
	line_count = 0
	docNumber_count = 20000000
	docNumbers = []
	names = []
	lastnames = []
	person = []
	birth_dates = []
	
	with open('C:\\Users\\ASUS-K555U\\Downloads\\nombres-1975-1979.csv') as csv_file:
		csv_names = csv.reader(csv_file, delimiter=',')

		for csv_name in csv_names:
			if line_count == 0:
				#print(f'{line_count} Column names are {", ".join(csv_name)}')
				names.append(csv_name[0])
				docNumbers.append(str(docNumber_count))
				birth_dates.append(dateFrom - timedelta(days=line_count+3))
				line_count += 1
				docNumber_count += 7
			else:
				try:
					#print(f'{line_count}-\t{csv_name[0]}')
					names.append(csv_name[0])
					docNumbers.append(str(docNumber_count))
					birth_dates.append(dateFrom - timedelta(days=line_count+3))
					line_count += 1
					docNumber_count += 5
				except:
					print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
		print(f'Processed {line_count} lines.')

	with open('C:\\Users\\ASUS-K555U\\Downloads\\apellidos_mas_frecuentes.csv') as csv_file:
		csv_last_names = csv.reader(csv_file, delimiter=';')

		for csv_last_name in csv_last_names:

			if line_count == 0:
				#print(f'{line_count} Column names are {", ".join(csv_last_name)}')
				lastnames.append(csv_last_name[1])
				line_count += 1
			else:
				try:
					#print(f'{line_count}-\t{csv_last_name[1]}')
					lastnames.append(csv_last_name[1])
					line_count += 1
				except:
					print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
		print(f'Processed {line_count} lines.')

	for name in names:
		temp = []
		temp.append(name)	
		for lastname in lastnames[:]:
			randomLastname = random.choices(population=lastnames, k=1)
			temp.append(randomLastname[0])	
			#if(len(lastnames) > 1):
				#lastnames.remove(lastname)
			break		
		for doc in docNumbers[:]:
			temp.append(str(doc))
			docNumbers.remove(doc)
			break
		for date in birth_dates[:]:
			temp.append(str(date) + ' 00:00:00')
			birth_dates.remove(date)
			break
		person.append(temp)
	return person
	
startGetPersonsTime = datetime.now()
persons = getPersons()
endGetPersonsTime = datetime.now()
getPersonsTime = endGetPersonsTime - startGetPersonsTime
#print('getPersons - time: %s' % getPersonsTime)
#for full in persons:
	#print(full[0] + ', ' + full[1]+ ', ' + full[2]+ ', ' + full[3])

NUM_HILOS = 100
splitTimeA = datetime.now()
splitPersons = numpy.array_split(persons,NUM_HILOS);
splitTimeB = datetime.now()
splitTime = splitTimeB - splitTimeA
print('splitTime: %s' % splitTime)

def printPerson(p):
	print('Hilo:', threading.current_thread().getName(), 'con identificador:', threading.current_thread().ident, 'Person:', p[0])
	#print(p[0] + ', ' + p[1]+ ', ' + p[2]+ ', ' + p[3])

num_hilo = 0	
for personLists in splitPersons:
	num_hilo += 1
	print(num_hilo)
	for per in personLists:
		hilo = threading.Thread(name='%s' %num_hilo, target=printPerson(per))    		
		hilo.start()
#for num_hilo in range(NUM_HILOS):
    
	
