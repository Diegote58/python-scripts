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

print(normalize("¡Hólá, múndó!"))
print(normalize("¡HÓLÁ, MÚNDÓ!"))

def replace(phrase):
	remove = [' ','.','-','1','2','3','4','5','6','7','8','9']	
	cadena = normalize(phrase)
	for r in remove:
		cadena = cadena.replace(r,'')			

	return cadena
