import numpy as np
import matplotlib.pyplot as plt

i = 6
eppara = 0.5 * (10 ** (2 - i))

def f(x):
    return np.sin(x) + np.cos(1 + x**2) - 1

casos = [
    ("a", 1.0,  3.0),
    ("b", 1.5,  2.5),
    ("c", 1.5,  2.25),
]

# ---- SECANTE ----
raiz_casos = {}
for label, x0, x1 in casos:
    epest = 100
    iteracoes = 0

    while epest >= eppara:
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        epest = abs((x_new - x1) / x_new) * 100
        x0 = x1
        x1 = x_new
        iteracoes += 1

    raiz_casos[label] = x1
    print(f"Caso {label}: x = {x1:.6f} | erro = {epest:.2e} | iterações: {iteracoes}")

# ---- GRÁFICO GERAL ----
x_plot = np.linspace(0.01, 10, 1000)

cores = {'a': 'tomato', 'b': 'steelblue', 'c': 'seagreen'}

plt.figure(figsize=(10, 5))
plt.plot(x_plot, f(x_plot), color='black', lw=1.5, label=r'$f(x) = \sin(x) + \cos(1+x^2) - 1$')
plt.axhline(0, color='gray', lw=0.8, ls='--')

for label, raiz in raiz_casos.items():
    plt.axvline(raiz, color=cores[label], lw=0.8, ls=':')
    plt.plot(raiz, 0, 'o', color=cores[label], markersize=7, label=f'Caso {label}: x = {raiz:.4f}')

plt.title(r'$f(x) = \sin(x) + \cos(1+x^2) - 1$', fontsize=13)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.ylim(-3, 3)
plt.xlim(0, 10)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# ---- GRÁFICO ZOOM ----
x_zoom = np.linspace(0.5, 4.5, 1000)

plt.figure(figsize=(10, 5))
plt.plot(x_zoom, f(x_zoom), color='black', lw=1.5, label=r'$f(x) = \sin(x) + \cos(1+x^2) - 1$')
plt.axhline(0, color='gray', lw=0.8, ls='--')

for label, raiz in raiz_casos.items():
    plt.axvline(raiz, color=cores[label], lw=0.8, ls=':')
    plt.plot(raiz, 0, 'o', color=cores[label], markersize=7, label=f'Caso {label}: x = {raiz:.4f}')

plt.title(r'Zoom — região da 1ª raiz positiva', fontsize=13)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.ylim(-2.5, 2.5)
plt.xlim(0.5, 4.5)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
