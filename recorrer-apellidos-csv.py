import csv
from datetime import date, datetime, timedelta
line_count = 0
docNumber_count = 20000000
docNumbers = []
names = []
lastnames = []
person = []
birth_dates = []
date = date(1979, 7, 2)
with open('C:\\Users\\ASUS-K555U\\Downloads\\nombres-1975-1979.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')

	for row in csv_reader:
		if line_count == 0:
			#print(f'{line_count} Column names are {", ".join(row)}')
			names.append(row[0])
			docNumbers.append(str(docNumber_count))
			birth_dates.append(date - timedelta(days=line_count+3))
			line_count += 1
			docNumber_count += 7
		else:
			try:
				#print(f'{line_count}-\t{row[0]}')
				names.append(row[0])
				docNumbers.append(str(docNumber_count))
				birth_dates.append(date - timedelta(days=line_count+3))
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
	for date in birth_dates[:]:
		temp.append(str(date) + ' 00:00:00')
		birth_dates.remove(date)
		break
	person.append(temp)
		
for full in person:
	print(full[0] + ', ' + full[1]+ ', ' + full[2]+ ', ' + full[3])
	
	
	
	

