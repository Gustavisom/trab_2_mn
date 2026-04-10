import numpy as np
import matplotlib.pyplot as plt

# ── Configurações ──────────────────────────────────────────────────────────────
i = 6
eppara = 0.5 * (10 ** (2 - i))   # critério de parada: 6 algarismos significativos

# ── Função e derivada ──────────────────────────────────────────────────────────
def f(x):
    return np.sin(x) + np.cos(1 + x**2) - 1

# ── Método da Secante ──────────────────────────────────────────────────────────
def secante(xi_1, xi, label):
    """
    Método da secante com critério de parada Epest (6 algarismos significativos).
    Retorna (raiz, iterações, histórico_x, histórico_epest) ou None se divergir.
    """
    historico_x     = [xi_1, xi]
    historico_epest = []
    iteracoes       = 0
    max_iter        = 100

    print(f"\n{'─'*55}")
    print(f"  {label}  |  xi-1 = {xi_1}  ,  xi = {xi}")
    print(f"{'─'*55}")
    print(f"  {'Iter':>4}  {'xi+1':>14}  {'f(xi+1)':>14}  {'Epest (%)':>12}")
    print(f"{'─'*55}")

    while iteracoes < max_iter:
        f_xi_1 = f(xi_1)
        f_xi   = f(xi)

        denom = f_xi - f_xi_1
        if abs(denom) < 1e-14:
            print("  ⚠  Denominador nulo — método falhou.")
            return None

        xi1 = xi - f_xi * (xi - xi_1) / denom

        # Epest só calculado a partir da 1ª iteração (xi1 != 0 teoricamente)
        if abs(xi1) > 1e-14:
            epest = abs((xi1 - xi) / xi1) * 100
        else:
            epest = abs(xi1 - xi) * 100

        historico_x.append(xi1)
        historico_epest.append(epest)
        iteracoes += 1

        print(f"  {iteracoes:>4}  {xi1:>14.8f}  {f(xi1):>14.2e}  {epest:>11.6f}%")

        if epest < eppara:
            print(f"{'─'*55}")
            print(f"  ✔  Convergiu em {iteracoes} iterações")
            print(f"  ✔  Raiz ≈ {xi1:.8f}   |   f(raiz) = {f(xi1):.2e}")
            return xi1, iteracoes, historico_x, historico_epest

        xi_1, xi = xi, xi1

    print("  ⚠  Máximo de iterações atingido sem convergência.")
    return None

# ── Executar os três casos ─────────────────────────────────────────────────────
casos = [
    (1.0,  3.0,  "a) xi-1 = 1.0 , xi = 3.0"),
    (1.5,  2.5,  "b) xi-1 = 1.5 , xi = 2.5"),
    (1.5,  2.25, "c) xi-1 = 1.5 , xi = 2.25"),
]

resultados = []
for xi_1, xi, label in casos:
    res = secante(xi_1, xi, label)
    resultados.append((label, xi_1, xi, res))

# ── d) Método Gráfico ──────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Exercício 2 — f(x) = sin(x) + cos(1 + x²) − 1", fontsize=13, fontweight='bold')

# --- Gráfico esquerdo: função no intervalo amplo ---
ax = axes[0]
x_vals = np.linspace(0.01, 10, 2000)
y_vals = f(x_vals)

ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax.plot(x_vals, y_vals, color='steelblue', linewidth=1.8, label='f(x)')
ax.set_xlim(0.01, 10)
ax.set_ylim(-3, 3)
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('f(x)', fontsize=11)
ax.set_title('Visão geral — raízes no intervalo (0, 10]', fontsize=10)
ax.legend()
ax.grid(True, alpha=0.3)

# Marca raízes encontradas com convergência
cores  = ['tomato', 'limegreen', 'darkorange']
marcas = ['o', 's', '^']
for idx, (label, _, _, res) in enumerate(resultados):
    if res is not None:
        raiz = res[0]
        ax.plot(raiz, f(raiz), marcas[idx], color=cores[idx],
                markersize=9, label=f'{label[:2]} raiz={raiz:.4f}', zorder=5)
ax.legend(fontsize=8)

# --- Gráfico direito: zoom na região da 1ª raiz positiva ---
ax2 = axes[1]
x_zoom = np.linspace(0.5, 4.5, 2000)
y_zoom = f(x_zoom)

ax2.axhline(0, color='black', linewidth=0.8, linestyle='--')
ax2.plot(x_zoom, y_zoom, color='steelblue', linewidth=1.8, label='f(x)')

# Pontos iniciais de cada caso
estilos_ci = [('tomato', 'o', '^'), ('limegreen', 's', 'D'), ('darkorange', '^', 'v')]
for idx, (label, xi_1_val, xi_val, res) in enumerate(resultados):
    c = cores[idx]
    ax2.plot(xi_1_val, f(xi_1_val), 'x', color=c, markersize=10, markeredgewidth=2,
             label=f'{label[:2]} xi-1={xi_1_val}')
    ax2.plot(xi_val,   f(xi_val),   '+', color=c, markersize=12, markeredgewidth=2,
             label=f'{label[:2]} xi={xi_val}')
    if res is not None:
        raiz = res[0]
        ax2.plot(raiz, 0, marcas[idx], color=c, markersize=10, zorder=5,
                 label=f'{label[:2]} raiz≈{raiz:.4f}')

ax2.set_xlim(0.5, 4.5)
ax2.set_ylim(-2.5, 2.5)
ax2.set_xlabel('x', fontsize=11)
ax2.set_ylabel('f(x)', fontsize=11)
ax2.set_title('Zoom — região da 1ª raiz positiva', fontsize=10)
ax2.legend(fontsize=7, ncol=2)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ex2_grafico.png', dpi=150, bbox_inches='tight')
plt.show()
print("\n✔ Gráfico salvo em ex2_grafico.png (mesma pasta do script)")
