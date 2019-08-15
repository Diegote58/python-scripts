def findFirstMaxIndex(list, max):           
	index = 0
	for x in list:
		if (x == max):
			print("index %s, valor %s, maximo %s" % (index,x,max))			
			break
		index += 1
	return index
list = [1,3,4]
print(list)
max = max(list)
print(max)
max_index = findFirstMaxIndex(list,max)
print(max_index)

