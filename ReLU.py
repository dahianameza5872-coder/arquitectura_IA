def ReLU(x):
    return max(0, x)
#Grafica
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = [ReLU(i) for i in x]
plt.plot(x, y)
plt.title('ReLU Function')
plt.xlabel('x')
plt.ylabel('ReLU(x)')
plt.grid()
plt.show()

