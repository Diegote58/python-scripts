import threading
import numpy
import multiprocessing
def contar():
    contador = 0
    while contador<100:
        contador+=1
        print('Hilo:', 
              threading.current_thread().getName(), 
              'con identificador:', 
              threading.current_thread().ident,
              'Contador:', contador)

NUM_HILOS = 3

for num_hilo in range(NUM_HILOS):
    hilo = threading.Thread(name='hilo%s' %num_hilo, target=contar)    
    hilo.start()
	
def printValue(s):
	print('Hilo:', threading.current_thread().getName(), 'con identificador:', threading.current_thread().ident, 'Value:', s)
	#print(p[0] + ', ' + p[1]+ ', ' + p[2]+ ', ' + p[3])

num_hilo = 0	
array = ['1','3','4','A','V','X','4','Z']
split = numpy.array_split(array,6);
threads = []
for sp in split:
	num_hilo += 1
	for s in sp:
		hilo = threading.Thread(name='%s' %num_hilo, target=printValue(s))  		
		threads.append(hilo)		
		#for s in sp:

for t in threads:
	t.start()        
		