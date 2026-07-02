import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

# Fase (phi) induzida pelo cristal Pockels
phi = np.linspace(-np.pi, np.pi, 400)

# 1. Sem QWP (Sem bias): I = cos^2(phi/2)
# O ponto de operação é phi=0 (topo da curva, região insensível)
int_sem_qwp = np.cos(phi / 2)**2

# 2. Com QWP (Bias de pi/2): I = cos^2((phi + pi/2)/2)
# Isso introduz um deslocamento de fase de pi/2 (90 graus) no argumento
# Agora, em phi=0, temos cos^2(pi/4) = 0.5 (ponto de quadratura)
int_com_qwp = np.cos((phi + np.pi / 2) / 2)**2 

# Configuração para formatar o eixo X em pi
def format_func(value, tick_number):
    N = int(np.round(value / (np.pi / 2)))
    if N == 0: return "0"
    elif N == 1: return r"$\pi/2$"
    elif N == -1: return r"$-\pi/2$"
    elif N == 2: return r"$\pi$"
    elif N == -2: return r"$-\pi$"
    return f"{N}π/2"

# Plotagem
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(phi, int_sem_qwp, label='Without QWP', color='red', linestyle='--', alpha=0.7)
ax.plot(phi, int_com_qwp, label='With QWP', color='blue', linewidth=2)

# Ajuste do eixo X
ax.xaxis.set_major_locator(MultipleLocator(np.pi / 2))
ax.xaxis.set_major_formatter(FuncFormatter(format_func))

# Linhas de referência
ax.axvline(0, color='gray', linestyle=':', alpha=0.5)
ax.axhline(0.5, color='gray', linestyle=':', alpha=0.5, label='Ponto Médio (0.5)')

ax.set_title('Phase shift $\pi/2$ (90°) com QWP')
ax.set_xlabel('Phase induced by QWP (rad)')
ax.set_ylabel('Light intensity (output))')
ax.legend()
ax.grid(True, alpha=0.3)

plt.show()