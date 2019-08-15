import requests
import json
import re
def normalizeDescription(description):	
	if(re.search("<div.*?'>",description)):
		print("search")
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
	
def parseDescription():
	description = "<div style='text-align:left;'><b>Móvil:</b> Sol Bus int 116<br /><b>Empresa:</b> Sol Bus<br /><b>Velocidad:</b> 30 K/h <br /> <b>Dirección:</b> SurEste<br /><b>Última transmisión:</b> 20/06/2019 01:28:35 p.m.</div>"
	return normalizeDescription(description)
	
	
#parseObject()
parseDescription()
