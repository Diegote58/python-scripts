import random
somelist = ['1','3','4']
#for x in somelist:
	#somelist.remove(x)
#somelist [1, 3, 5, 7, 9]
b = '1'
for x in somelist[:]:
	print ("comparing %s with %s: %s" % (b, x, x.lower() == b.lower()))
	if(x.lower() == b.lower()):
		somelist.remove(x)
#somelist[]
print(somelist)

for x in somelist[:]:
	print ("random: %s" % random.choise(somelist))
	
		