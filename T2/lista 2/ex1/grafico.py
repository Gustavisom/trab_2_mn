import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(4*x) + np.cos(3*x)

x = np.linspace(0, 2*np.pi, 1000)
y = f(x)

plt.plot(x, y)
plt.axhline(0, color='black')
plt.grid()
plt.show()