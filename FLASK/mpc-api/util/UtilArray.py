import re
import datetime
import time

def removeArray(array, removeArray):
	start = datetime.datetime.now()		
	for r in removeArray[:]:
		for x in array[:]:			
			if(x[0].lower() == r.lower()):
				#print ("comparing %s with %s: %s" % (r, x[0], x[0].lower() == r.lower()))
				array.remove(x)
	end = datetime.datetime.now()
	final = end - start
	#print("time -> removeArray: %s" % final)
	return array
	
#Elimina acentos y ':' del array
def normalizeKey(s):
	start = datetime.datetime.now()	
	replacements = (("á", "a"),("é", "e"),("í", "i"),("ó", "o"),("ú", "u"),(":", ""),)
	for a, b in replacements:
		s = s.lower().replace(a, b).replace(a.lower(), b.lower())
	end = datetime.datetime.now()
	final = (end - start)
	print("time -> normalizeKey: %s" % final)
	return s.lower()

#Elimina etiquetas HTML y hace split para formar un Map<k,v>
def normalizeDescription(description):
	start = datetime.datetime.now()	
	description = (re.sub("<div.*?'>", "", description))	
	description = description.replace("</div>", "")	
	description = description.replace("<b>", "")	
	splits = description.split("<br />")
	descriptionMap = {}
	for sp in splits:	
		kv = sp.split("</b>")
		#print(kv)
		key = normalizeKey(kv[0].strip())
		value = kv[1].strip()
		descriptionMap[key] = value
	#for k,v in descriptionMap.items():
		#print("key: %s, value: %s" % (k,v))
	end = datetime.datetime.now()
	final = end - start
	print("time -> normalizeDescription: %s" % final)
	return descriptionMap

#Split de csv por \n formando las filas
def splitCsv(rows):  
	start = datetime.datetime.now()
	rows = re.split(r"([\n])",rows)	
	#print("******** splitCsv: %s " % len(rows))
	#for ln in rows:
		#print(ln)
	end = datetime.datetime.now()
	final = end - start
	print("time -> splitCsv: %s" % final)
	return rows

#Split de filas por \t array de valores
def splitRow(row):  
	start = datetime.datetime.now()
	result = re.split(r"([\t])",row)
	#print("******** splitRow: %s " % len(result))
	#for row in result:
		#print(row)
	end = datetime.datetime.now()
	final = end - start
	print("time -> splitRow: %s" % final)
	return result

#Filtra valores del array quitando '','\t' y '\n'
def filter(line):  
	start = datetime.datetime.now()
	rows = splitCsv(line)
	result = []
	for row in rows:
		#Elimino falso array con ['\n']
		if('\n' not in row):
			result.append(splitRow(row))
	for row in result[:]:
		for r in row[:]:
			#Elimino valores == ['\t'] del array
			if('\t' == r or '' == r):
				row.remove(r)				
		#print(row)
	end = datetime.datetime.now()
	final = end - start
	print("time -> filter: %s" % final)
	return result
