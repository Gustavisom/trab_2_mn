import numpy as np

def f(x):
    return np.sin(4*x) + np.cos(5*x) + 1/x

i = 6
eppara = 0.5 * (10 ** (2 - i))

x = np.linspace(0, 2*np.pi, 1000)
intervalos = []

for i in range(len(x)-1):
    if f(x[i]) * f(x[i+1]) < 0:
        intervalos.append([x[i], x[i+1]])

print(f"Intervalos encontrados: {len(intervalos)}\n")

for idx, (xl, xu) in enumerate(intervalos):
    x0 = xl
    x1 = xu
    epest = 100
    iteracoes = 0

    while epest >= eppara:
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        epest = abs((x_new - x1) / x_new) * 100
        x0 = x1
        x1 = x_new
        iteracoes += 1

    print(f"Raiz {idx+1}: x = {x1:.6f} | f(x) = {f(x1):.2e} | iterações: {iteracoes}")
    