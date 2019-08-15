from json import JSONEncoder
import json
		
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
			
def busesToJSON(buses):
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
	print("time -> busesToJSON: %s" % final)
	return result