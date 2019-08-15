nombres = ['Maria','Mario','martin','Emilia']

#print ("%s == %s: %s" % (nombre[-1:], 'a', 'a'.lower() == nombre[-1:].lower()))

for nombre in nombres:
	if ('a'.lower() == nombre[-1:].lower()):
		print('F')
	else:
		print('M')
	
#print('F') if ('a'.lower() == nombre[-1:].lower()) else print('M')	
	
