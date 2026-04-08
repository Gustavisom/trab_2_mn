import numpy as np


def f(x):
    return np.sin(4*x) + np.cos(5*x) + 1/x

def df(x):
    return 4*np.cos(4*x) - 5*np.sin(5*x) - 1/x**2

epest = 100
i = 6
eppara = 0.5 * (10 ** (2 - i))
x0 = 0

def newton_raphson(f, df, x0, tol=1e-10, max_iter=100):
    x = x0 if x0 != 0 else 0.0001  
    for i in range(max_iter):
        x_new = x - f(x)/df(x)
        epest = abs(x_new - x)
        if epest < tol:
            return x_new
        x = x_new
        
while epest > eppara:
    raiz = newton_raphson(f, df, x0)
    print(f"{raiz}")
