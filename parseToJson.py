import requests
import json
import re


class MiProximoColectivo(map):
	latitude = ["latitude"]
	longitude = ["latitude"]
	title = ["title"]
	description	= ["latitude"]
	icon = ["icon"]
	iconSize = ["iconSize"]
	iconOffset = ["iconOffset"]
		
def removeArray(array, removeArray):
	for r in removeArray[:]:
		for x in array[:]:			
			if(x[0].lower() == r.lower()):
				#print ("comparing %s with %s: %s" % (r, x[0], x[0].lower() == r.lower()))
				array.remove(x)
	return array
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.lower(), b.lower())
    return s.lower()
def normalizeDescription(description):	
	description = (re.sub("<div.*?'>", "", description))	
	description = description.replace("</div>", "")	
	description = description.replace("<b>", "")	
	splits = description.split("<br />")
	descriptionMap = {}
	for sp in splits:	
		kv = sp.split("</b>")
		#print(kv)
		descriptionMap[kv[0]] = kv[1]
	for k,v in descriptionMap.items():
		print("key: %s, value: %s" % (k,v))
	return descriptionMap
		
def parseObject():
	remove = ['lat', 'lon', 'title', 'description', 'icon', 'iconSize', 'iconOffset','']
	array = [['lat'], ['lon'], ['title'], ['description'], ['icon'], ['iconSize'], ['iconOffset'], 
		['-33.35315'], ['-60.191'], ['Sol Bus int 116'], ["<div style='text-align:left;'><b>Móvil:</b> Sol Bus int 116<br /><b>Empresa:</b> Sol Bus<br /><b>Velocidad:</b> 30 K/h <br /> <b>Dirección:</b> SurEste<br /><b>Última transmisión:</b> 20/06/2019 01:28:35 p.m.</div>"], ['/Images/ico_bus/1/1_Seste.png'], ['25,25'],['-12,-15'], 
		['-33.1783525'], ['-66.2941931666667'], ['Sol Bus int 127'], ["<div style='text-align:left;'><b>Móvil:</b> Sol Bus int 127<br /><b>Empresa:</b> Sol Bus<br /><b>Velocidad:</b> 33 K/h <br /> <b>Dirección:</b> Este<br /><b>Última transmisión:</b> 20/06/2019 01:30:08 p.m.</div>"], ['/Images/ico_bus/1/1_este.png'], ['25,25'], ['-12,-15'], 
		['-33.2990646666667'], ['-66.3221801666667'], ['Sol Bus int 123'], ["<div style='text-align:left;'><b>Móvil:</b> Sol Bus int 123<br /><b>Empresa:</b> Sol Bus<br /><b>Velocidad:</b> 38 K/h <br /> <b>Dirección:</b> Sur<br /><b>Última transmisión:</b> 20/06/2019 01:30:14 p.m.</div>"], ['/Images/ico_bus/1/1_Sur.png'], ['25,25'], ['-12,-15'], 
		['-33.1784905'], ['-66.319554'], ['Sol Bus int 122'], ["<div style='text-align:left;'><b>Móvil:</b> Sol Bus int 122<br /><b>Empresa:</b> Sol Bus<br /><b>Velocidad:</b> 24 K/h <br /> <b>Dirección:</b> SurOeste<br /><b>Última transmisión:</b> 20/06/2019 01:30:09 p.m.</div>"], ['/Images/ico_bus/1/1_Soeste.png'], ['25,25'], ['-12,-15'],
		['-33.2607095'], ['-66.2990343333333'], ['Sol Bus int 124'], ["<div style='text-align:left;'><b>Móvil:</b> Sol Bus int 124<br /><b>Empresa:</b> Sol Bus<br /><b>Velocidad:</b> 0 K/h <br /> <b>Dirección:</b> Norte<br /><b>Última transmisión:</b> 20/06/2019 01:21:43 p.m.</div>"], ['/Images/ico_bus/1/1_Norte_alto.png'], ['25,25'], ['-12,-15']]
	array = removeArray(array,remove)

	return array

#parseObject()
n = normalizeDescription()
print(n)
