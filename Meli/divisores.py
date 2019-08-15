
#PROGRAMA PARA FACTORIZAR##NÚMEROS NATURALES Y HALLAR##TODOS SUS DIVISORES.#
from math import sqrt
#Importa la función raíz cuadrada del módulo math
# función factorizar. input n integer. output una lista# con los factores primos de n
def factorizar(n):
	factores=[] 
	# lista de los factores primos
	flag = True
	while flag:
		k = int(sqrt(n))
		for p in range(2,k+1):
			r = n%p
			q = int((n-r)/p)
			if r == 0:
				factores.append(p)
				n = q
				break
			if p == k:
				factores.append(n)
				flag = False
	return factores
		
# Calcula todos los divisores de un número a partir de su descomposición en factores primos.
def divisores(m):
	#función para obtener los divisores
	factor = factorizar(m)
	#input: un número entero positivo 
	mdivisor = [1]
	#output: una lista (divisor) con los divisores de 
	mpotencias=[]
	n = len(factor)
	i = 0
	while i < n : 
		p = factor[i]
		pot = [p]
		d = p
		i += 1
		while i < n and p == factor[i]: 
			#este bucle calcula todas las potenciasde#de un factor primo 
			d = d*p		
			dadopot.append(d)
			i += 1
			potencias.append(pot)
	for a in potencias:
		n=len(divisor)
		for p in a:
			for j in range(n):
				divisor.append(divisor[j]*p)
	return divisor
	
def intro_num():
	print('-'*60)
	m=int(float(input('Introduce un número>')))
	while m<=0:
		print('Debes introducir un número entero positivo.')
		print('-'*60)
		m=int(float(input('Introduce un número>')))
	return m
	
def ordenar(a):
	#para ordenar una lista de números a
	n=len(a) 
	#empleando el algoritmo de la burbuja
	flag=False
	i=0
	while(i < n or flag==False):
		i += 1
		flag=True
		for j in range(n-i):
			if a[j]>a[j+1]:
				flag=False
				aux=a[j+1]
				a[j+1]=a[j]
				a[j]=aux
	return a
	
	
# CUERPO PRINCIPAL DEL PROGRAMA
while True:
	print('-'*60) 
	#esto es el menú para el usuario.
	print('a) Factorizar un número')
	print('b) Calcular los divisores de un número.')
	print('c) Salir')
	print('-'*60)
	opcion=input('Introduce una opción>')
	if opcion=='a':
		m = intro_num()
		print('-'*60)
		print('Los factores primos de %s son %s' % (m,factorizar(m)))
	elif opcion=='b':
		m=intro_num()
		print('-'*60)
		print('Los divisores del número',m,'son:')
		print(ordenar(divisores(m)))
	elif opcion=='c': break
	else:
		print('-'*60)
		print('Debes introducir una opción.')