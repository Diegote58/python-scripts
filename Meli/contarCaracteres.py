
cadena = "Holá, mi nombre es ariel, soy una sirenita, vivo bajo el mar"
cadena = cadena.lower()
letra = ""
diccionario = ['A','O','U']
ocurrencias = 0
for d in diccionario:
	if(ocurrencias < cadena.count(d.lower())):
		letra = d
		ocurrencias = cadena.count(d.lower())
	
print("letra: %s, occ %s" % (letra,ocurrencias))
ocurrencias = cadena.count("o")
print(ocurrencias)
