import numpy
array = ['1','3','4','A','V','X','4','Z']
split = numpy.array_split(array,6);
print(array)
for sp in split:
	print(sp)
	for s in sp:
		print(s)