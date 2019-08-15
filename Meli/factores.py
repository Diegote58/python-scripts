from math import sqrt

def factores(n):
	factores=[] 
	for p in range(1,n + 1):
		if (n % p == 0):
			factores.append(p)					
	return factores
	
def intro_num(op):
	print('-'*60)
	m = 0
	if(op == 'a'):
		m = int(float(input('Introduce un número: ')))
		while m <= 0:
			print('Debes introducir un número entero positivo.')
			print('-'*60)
			m=int(float(input('Introduce un número>')))
	if(op == 'b'):
		m = int(float(input('Introduce posicion del factor: ')))
		while m <= 0:
			print('Debes introducir un número entero positivo.')
			print('-'*60)
			m=int(float(input('Introduce un número')))	
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

def getFactor(position, factores):
	
	if(len(factores) < position):
		return 0
	return factores[position - 1]
	
m = intro_num('a')
factores=factores(m)

print('Los factores primos de %s son %s' % (m,factores))
m = intro_num('b')
print('Factor en la posición %s es: %s' % (m,getFactor(m,factores)))
	