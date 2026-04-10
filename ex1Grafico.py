from cProfile import label

import numpy as np
import matplotlib.pyplot as plt
import math


def f(x):
    return np.sin(4*x) + np.cos(5*x) + 1/x

#Aqui substituimos os termos Xu (upper = 2pi) e Xl (lower 0) para facilitar o entendimento

x = np.linspace(0, 2*math.pi, 1000 )
y = f(x)

# Esse trecho não faz parte do programa em si, apenas destaca os pontos onde estão as raízes
raizes = []
for i in range(len(y)-1):
    if y[i] * y[i+1] < 0:
        raizes.append((x[i] + x[i+1]) / 2)
        
plt.figure(figsize=(10, 5))
plt.plot(x, y, label=r'$f(x) = \sin(4x) + \cos(5x) + \frac{1}{x}$', color='blue')
plt.axhline(0, color='red', lw=0.8, ls='--', label=r'$f(x) = 0$')

plt.title(r'$ f(x) = \sin(4x) + \cos(5x) + \frac{1}{x}$ ', fontsize=14)
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

