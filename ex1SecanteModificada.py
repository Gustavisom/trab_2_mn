import numpy as np

def f(x):
    return np.sin(4*x) + np.cos(5*x) + 1/x

i = 6
eppara = 0.5 * (10 ** (2 - i))
delta = 0.0000001

x = np.linspace(0, 2*np.pi, 1000)
intervalos = []

for i in range(len(x)-1):
    if f(x[i]) * f(x[i+1]) < 0:
        intervalos.append([x[i], x[i+1]])

print(f"Intervalos encontrados: {len(intervalos)}\n")

for idx, (xl, xu) in enumerate(intervalos):
    x0 = (xl + xu) / 2
    epest = 100
    iteracoes = 0

    while epest >= eppara:
        x_new = x0 - f(x0) * (delta * x0) / (f(x0 + delta * x0) - f(x0))
        epest = abs((x_new - x0) / x_new) * 100
        x0 = x_new
        iteracoes += 1

    print(f"Raiz {idx+1}: x = {x0:.6f} | f(x) = {f(x0):.2e} | iterações: {iteracoes}")