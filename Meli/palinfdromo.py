def palindrome(word):
	long = (len(word)//2)	
	print("long: %s, long/2: %s" % (len(word),long))
	word = replace(word)
	long = (len(word)//2)	
	print("long: %s, long/2: %s" % (len(word),long))
	for i in range(long):
		if word[i] != word[-1-i]:
			return False
	return True

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s
	
def replace(phrase):
	remove = [' ','.','-','1','2','3','4','5','6','7','8','9']	
	cadena = normalize(phrase)
	for r in remove:
		cadena = cadena.replace(r,'')			

	return cadena



input = input("Ingrese la palabra para saber si es palindromo:")
print (normalize(input))
#print (palindrome(input))
