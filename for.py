names = ['pepe','lolo']
lastnames = ['Muleiro','Martinez','Muleiro','Martinez','Muleiro','Martinez','Muleiro','Martinez','Muleiro','Martinez']
cubes = [lastname + ', ' + name for lastname in lastnames for name in names]
#print(cubes)

transpose = []
for name in lastnames:
	temp = []
	temp.append(name)
	for lastname in names:
		temp.append(lastname)
		break
	transpose.append(temp)		
		
	
#print(temp)
print(transpose)