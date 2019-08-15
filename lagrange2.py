
# Python3 code to demonstrate  
# to get random number from list 
# using random.choice() 
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
import numpy as np


#x_i1 = [0.0, 0.9, 1.8, 2.7, 3.6, 4.4, 5.3, 6.2, 7.1, 8.0]
#y_i1 = [0.0, 0.8, 1.0, 0.5, -0.4, -1.0, -0.8, -0.1, 0.7, 1.0]
#x_i = [2,3,4,5,6,7]
#y_i = [0.5,0.3333,0.25,0.2,0.1667,1.1429]
x_i = [1,-3,5,7]
y_i = [-2,1,2,-3]
plt.plot(x_i, y_i, 'o', mew=2, label="Datos reales")
#plt.show()

# Cálculo de lo polinomio interpolante
lag_pol = lagrange(x_i, y_i)
print(lag_pol)

x = np.linspace(x_i[0], x_i[-1])
plt.plot(x, lag_pol(x))
plt.plot(x_i, y_i, 'x', mew=2, label="Otros Datos")
plt.legend()
plt.show()