
# Python3 code to demonstrate  
# to get random number from list 
# using random.choice() 
from scipy.interpolate import lagrange
import matplotlib.pyplot as pyplot

x = [2,3,4,5,6,7]
y = [0.5,0.3333,0.25,0.2,0.1667,1.1429]

pyplot.plot(x,y,"o")
pyplot.xlabel("X")
pyplot.ylabel("Y")
pyplot.show()
#pyplot.label("Interpolacion por Lagrange")


lagrange = lagrange(x,y)
print(lagrange)
print("Evaluar en X")
print(lagrange(4))
print(lagrange(2))
print(lagrange(6))