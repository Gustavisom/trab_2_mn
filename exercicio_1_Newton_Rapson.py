import numpy as np

def f(x):
    return np.sin(4*x) + np.cos(5*x) + 1/x

def df(x):
    return 4*np.cos(4*x) - 5*np.sin(5*x) - 1/x**2

i = 6
eppara = 0.5 * (10 ** (2 - i))

x = np.linspace(0, 2*np.pi, 1000)
intervalos = []

for i in range(len(x)-1):
    if f(x[i]) * f(x[i+1]) < 0:
        intervalos.append([x[i], x[i+1]])

print(f"Intervalos encontrados: {len(intervalos)}\n")

for idx, (xl, xu) in enumerate(intervalos):
    epest = 100
    x = (xl + xu) / 2  
    iteracoes = 0

    while epest >= eppara:
        x_new = x - f(x) / df(x)
        epest = abs((x_new - x) / x_new) * 100

        x = x_new
        iteracoes += 1

    print(f"Raiz {idx+1}: x = {x:.6f} | f(x) = {f(x):.2e} | iterações: {iteracoes}")