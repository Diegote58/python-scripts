def findFirstMaxIndex(list, max):           
	index = 0
	for x in list:
		if (x == max):
			#print("index %s, valor %s, maximo %s" % (index,x,max))			
			break
		index += 1
	return index
	
def check(list, max):           
	for x in list:
		#print("x: %s != max: %s" % (x,max))
		if (max != x):
			return True 
	return False
	
def recorrer(list):	
	result = []
	max_index = findFirstMaxIndex(list,max(list))	
	for i in range(0,len(list)):
		if (max_index == i):
			result.append(list[i])			
		else: 
			result.append(list[i] + 1)		
	#print("return %s" % (result))	
	return result

def recorrerLista(list):	
	iteraciones = 0
	max_index = findFirstMaxIndex(list,max(list))	
	result = check(list,max(list))
	print("Iteracion %s, Lista %s " % (iteraciones,list))
	while(result):			
		iteraciones += 1		
		list = recorrer(list)
		print("Iteracion %s, Lista %s " % (iteraciones,list))	
		max_index = findFirstMaxIndex(list,max(list))					
		result = check(list,max(list))				
		
lista = [1,3,3]
recorrerLista(lista)

