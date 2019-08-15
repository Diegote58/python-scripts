# archivo-entrada.py
import re
pattern = re.compile(r'\<.*?>')
def regex(regex, replace, line):  
	line = re.sub(regex, replace, line)	
	return line
	
def split(line):  
	line = re.split(r"([\t])",line)		
	return line
	
def normalize(s):
	replacement = ["<div.*?>", "</div>","<br />","<br/>","<br >","<br>","</b>","<b>"]
	for a in replacement:
		s = s.replace(a,"")
	return s
	
file = open ('mpc.txt','r')
header = file.readline()
print(header)
first = file.readline()
#replace = normalize(first)
#print(replace)
splits = split(first)
#first = normalize(first)
#print(first)
#first = regex(pattern,",", first)
#print(first)


for s in splits:
	if('\t' not in s):
		print(split(s))
file.close()