from cProfile import label

import numpy as np
import matplotlib.pyplot as plt
import math


limite_inferior = 0
limite_superior = 2*math.pi
passo = 100
x = np.arange(limite_inferior, limite_superior, passo)


def f(x):
    return np.sin(x) + np.cos(5*x) + 1/x


x = np.linspace(0, 2*math.pi, 100 )
y = f(x)

raizes = []
for i in range(len(y)-1):
    if y[i] * y[i+1] < 0:
        raizes.append((x[i] + x[i+1]) / 2)
        
plt.figure(figsize=(10, 5))
plt.plot(x, y, label=r'$f(x) = \sin(x) + \cos(5x) + \frac{1}{x}$', color='blue')
plt.axhline(0, color='red', lw=0.8, ls='--', label=r'$f(x) = 0$')

plt.title(r'$ f(x) = \sin(x) + \cos(5x) + \frac{1}{x}$ ', fontsize=14)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.ylim(-8, 8)  
plt.legend(fontsize=11)
plt.grid(alpha=0.4)
plt.tight_layout()

for r in raizes:
    plt.plot(r, 0, 'go', markersize=5, label='Raiz')
plt.tight_layout()
plt.show()

