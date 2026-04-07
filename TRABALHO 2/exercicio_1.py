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

plt.figure()
plt.plot(x, y, label='Função')
plt.axhline(0, color='red', lw=0.5, ls='--')
plt.title('Busca Incremental')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()



n = 100
x = np.linspace(0, 2*np.pi, n)
xb = []
nb = 0


for i in range(n-1):
    xl = x[i]
    xu = x[i+1]

    if (f(xl) * f(xu) < 0):
        nb += 1
        xb.append([xl, xu])
    else:    
        print("Não há raiz entre", xl, "e", xu)

print("xb = ", xb)
print("y =", f(x))
print("Número de intervalos com raiz:", nb)