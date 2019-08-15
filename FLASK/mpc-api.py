from json import JSONEncoder
import json
import requests
import re
import datetime
import time
from flask import Flask, request
app = Flask(__name__)

class Description:
	def __init__(this, movil, empresa, velocidad, direccion,lastUpdate):    
		this.movil = movil
		this.empresa = empresa
		this.velocidad = velocidad
		this.direccion = direccion
		this.lastUpdate	= lastUpdate
	

def description_creator(map):
	return Description(map['movil'],map['empresa'],map['velocidad'],map['direccion'],map['ultima transmision'])

class MiProximoColectivo:
	def __init__(this, latitude, longitude, title, description, icon, iconSize, iconOffset):    
		this.latitude = latitude
		this.longitude = longitude
		this.title = title
		this.Description = description
		this.icon = icon
		this.iconSize = iconSize
		this.iconOffset = iconOffset	
			
class JSONEncoder(JSONEncoder):	
	def default(self, object):
		if isinstance(object, MiProximoColectivo):
			return object.__dict__
		elif isinstance(object, Description):
			return object.__dict__
		else:
			# call base class implementation which takes care of
			# raising exceptions for unsupported types
			return json.JSONEncoder.default(self, object)

def removeArray(array, removeArray):
	start = datetime.datetime.now()		
	for r in removeArray[:]:
		for x in array[:]:			
			if(x[0].lower() == r.lower()):
				#print ("comparing %s with %s: %s" % (r, x[0], x[0].lower() == r.lower()))
				array.remove(x)
	end = datetime.datetime.now()
	final = end - start
	print("time -> removeArray: %s" % final)
	return array
	
def normalize(s):
	start = datetime.datetime.now()	
	replacements = (("á", "a"),("é", "e"),("í", "i"),("ó", "o"),("ú", "u"),(":", ""),)
	for a, b in replacements:
		s = s.lower().replace(a, b).replace(a.lower(), b.lower())
	end = datetime.datetime.now()
	final = (end - start)
	print("time -> normalize: %s" % final)
	return s.lower()
	
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
		key = normalize(kv[0].strip())
		value = kv[1].strip()
		descriptionMap[key] = value
	#for k,v in descriptionMap.items():
		#print("key: %s, value: %s" % (k,v))
	end = datetime.datetime.now()
	final = end - start
	print("time -> normalizeDescription: %s" % final)
	return descriptionMap
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

def parseObject(buses):
	start = datetime.datetime.now()
	result = []
	for bus in buses:
		print(len(bus))
		if(len(bus) == 7):
			#print("BUS \n %s" % (bus[3]))
			if(re.search("<div.*?'>",bus[3])):
				map = normalizeDescription(bus[3])
				#for k,v in map.items():
					#print("key: %s, value: %s" % (k,v))								
				description = description_creator(map)										
				mpc = MiProximoColectivo(bus[0],bus[1],bus[2], description, bus[4], bus[5], bus[6])
				result.append(mpc)
	end = datetime.datetime.now()
	final = end - start
	print("time -> parseObject: %s" % final)
	return result
	
@app.route('/miProximoColectivo')
def getMiProximoColectivoController():
	start = datetime.datetime.now()
	params = request.args.get('bbox')	
	url = 'https://miproximocolectivo.sanluis.gob.ar/MiProximoColectivo/GetMapMovilRecorrido?bbox=%s,%s,%s,%s' % (params[0],params[1],params[2],params[3])			
	headers = {'Content-type': 'application/json'}	
	response = requests.get(url,headers=headers)
	result = response.text
	end = datetime.datetime.now()
	final = end - start
	buses = filter(result)
	bs = parseObject(buses)	
	
	print("time -> getMiProximoColectivoController: %s" % final)
	return JSONEncoder().encode(bs)
	
if __name__ == '__main__':
    app.run()