import re

def regex(regex, replace, line):  
	line = re.sub(regex, replace, line)	
	return line
	
print("Hola<--->")
pattern = re.compile(r'\<.*?>')
a = regex(pattern,"5","Hola<--->")
print(a)