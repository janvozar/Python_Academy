# import mumpy + matplotlib
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    x = 2 * x + 5
    return y

x = np.arange(0.10)
y = func(x)

plt.title ('Nadpis')
plt.xlabel('x label')
plt.ylabel('y label')

plt.plot(x,y)
plt.show()