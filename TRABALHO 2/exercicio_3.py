import numpy as np

# Dados
rho = 1.23        # kg/m³
mu = 1.79e-5      # N·s/m²
D = 0.005         # m
V = 40            # m/s
L = 0.2           # m
eps_a = 0.0015e-3 # m (tubo liso, 0.0015 mm)
eps_b = 0.045e-3  # m (aço comercial, 0.045 mm)

i = 6
eppara = 0.5 * (10 ** (2 - i))
delta = 0.01

# Reynolds
Re = rho * V * D / mu
print(f"Re = {Re:.2f}")

# Chute inicial de Blasius
f0 = 0.316 / Re**0.25
print(f"f0 Blasius = {f0:.6f}\n")

def colebrook(f, eps):
    return 1/np.sqrt(f) + 2*np.log10(eps/(3.7*D) + 2.51/(Re*np.sqrt(f)))

def resolver(eps, label):
    x0 = f0
    epest = 100
    iteracoes = 0

    while epest >= eppara:
        x_new = x0 - colebrook(x0, eps) * (delta * x0) / (colebrook(x0 + delta * x0, eps) - colebrook(x0, eps))
        epest = abs((x_new - x0) / x_new) * 100
        x0 = x_new
        iteracoes += 1

    f_final = x0
    delta_p = f_final * (L * rho * V**2) / (2 * D)
    print(f"=== {label} ===")
    print(f"f = {f_final:.6f} | iterações: {iteracoes}")
    print(f"Δp = {delta_p:.2f} Pa\n")

resolver(eps_a, "a) Tubo liso (ε = 0.0015 mm)")
resolver(eps_b, "b) Aço comercial (ε = 0.045 mm)")