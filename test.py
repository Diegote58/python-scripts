import csv
import sys
import codecs
line_count = 0
names = []
lastnames = []
def printhello():
    print ("hello")
	
#and u'niño' are the same string.
print(u'ni\xf1o')
#with open('C:\\Users\\ASUS-K555U\\Downloads\\nombres-1975-1979.csv') as csv_file:
with open('C:\\Users\\ASUS-K555U\\Downloads\\apellidos_mas_frecuentes.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=';')

	for row in csv_reader:

		if line_count == 0:
			print(f'{line_count} Column names are {", ".join(row)}')
			line_count += 1
		else:
			try:
				print(f'{line_count}-\t{row[1]}')
				s = row[1]
				uu = s.encode('utf8')
				z = uu.decode('cp1250')
				names.append(u'%s' % s)
				line_count += 1
			except:
				print("*******************1234***************\n\n\n\n\n\n\n\n\n")				
			finally:
				print("**********************************\n")
				line_count += 1
	#print(f'Processed {line_count} lines.')
print('-----')
print('niño')


#for row in names:
	#print(row)		
	#print(f'Processed {line_count} lines.')
