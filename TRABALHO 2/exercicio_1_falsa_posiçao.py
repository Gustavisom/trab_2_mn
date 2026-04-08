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
    epest = 100
    xr_ant = xu - f(xu) * (xl - xu) / (f(xl) - f(xu))  
    iteracoes = 0

    while epest >= eppara:
        xr = xu - f(xu) * (xl - xu) / (f(xl) - f(xu))  
        f_xl = f(xl)
        f_xr = f(xr)

        if iteracoes > 0:
            epest = abs((xr - xr_ant) / xr) * 100

        if f_xr * f_xl < 0:
            xu = xr
        else:
            xl = xr

        xr_ant = xr
        iteracoes += 1

    print(f"Raiz {idx+1}: x = {xr:.6f} | f(x) = {f(xr):.2e} | iterações: {iteracoes}")