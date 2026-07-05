import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

# --- 1. Parâmetros e Cálculos ---
t = np.linspace(0, 2*np.pi, 200)
phi = np.pi/4  # Defasagem (apenas para o gráfico de onda)

# Sine waves
Ex_wave = np.sin(t)
Ey_wave = np.sin(t - phi)

# Vetor Inicial (45 graus, amplitude unitária)
angle = np.pi/4
input_vec = [np.cos(angle), np.sin(angle)]

# Phasors (Subplot 3: 90 graus entre eles, amplitudes 1 e 0.75)
vec_x = [1, 0]      # Amplitude 1
vec_y = [0, 0.75]   # Amplitude 0.75

# Soma Fasorial
stat_res_x = vec_x[0] + vec_y[0]
stat_res_y = vec_x[1] + vec_y[1]

# --- 2. Configuração da Figura (2x2) ---
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
plt.subplots_adjust(wspace=0.3, hspace=0.3)

# 1. Input Vector (45°)
axs[0, 0].arrow(0, 0, input_vec[0], input_vec[1], head_width=0.15, head_length=0.15, fc='red', ec='red', width=0.03, length_includes_head=True)
axs[0, 0].set_xlim(-2, 2); axs[0, 0].set_ylim(-2, 2)
axs[0, 0].set_title("1. Vetor de Entrada (45°, Amp=1)")
axs[0, 0].set_aspect('equal'); axs[0, 0].grid(True)

# 2. Sine Waves over Time
axs[0, 1].plot(t, Ex_wave, label='Ex', color='red')
axs[0, 1].plot(t, Ey_wave, label='Ey (Delayed)', color='green', linestyle='--')
axs[0, 1].set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
axs[0, 1].set_xticklabels([r'$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
axs[0, 1].set_xlim(0, 2*np.pi); axs[0, 1].set_ylim(-1, 1)
axs[0, 1].set_title("2. Efeito no Cristal (Domínio do Tempo)")
axs[0, 1].legend(loc='upper right', fontsize='small'); axs[0, 1].grid(True)

# 3. Phasors (90° offset)
axs[1, 0].arrow(0, 0, vec_x[0], vec_x[1], head_width=0.15, head_length=0.15, fc='red', ec='red', width=0.03, length_includes_head=True, label='Vector X (Amp=1)')
axs[1, 0].arrow(0, 0, vec_y[0], vec_y[1], head_width=0.15, head_length=0.15, fc='green', ec='green', width=0.03, length_includes_head=True, label='Vector Y (Amp=0.75)')
axs[1, 0].arrow(0, 0, stat_res_x, stat_res_y, head_width=0.15, head_length=0.15, fc='blue', ec='blue', width=0.03, linestyle='--', length_includes_head=True, label='Soma')

# Parallelogram lines
axs[1, 0].plot([vec_x[0], stat_res_x], [vec_x[1], stat_res_y], 'k--', alpha=0.3)
axs[1, 0].plot([vec_y[0], stat_res_x], [vec_y[1], stat_res_y], 'k--', alpha=0.3)
axs[1, 0].set_xlim(-2, 2); axs[1, 0].set_ylim(-2, 2)
axs[1, 0].set_aspect('equal'); axs[1, 0].grid(True)
axs[1, 0].set_title("3. Fasores em quadratura (Snapshot)")
axs[1, 0].legend(fontsize='small', loc='upper right')

# 4. Beam Splitter Effect
axs[1, 1].arrow(0, 0, stat_res_x, stat_res_y, head_width=0.15, fc='blue', ec='blue', width=0.03, length_includes_head=True, label='Input (Sum)')
axs[1, 1].arrow(0, 0, stat_res_x, 0, head_width=0.15, fc='black', ec='black', width=0.03, linestyle=':', length_includes_head=True, label='Output H')
axs[1, 1].arrow(0, 0, 0, stat_res_y, head_width=0.15, fc='purple', ec='purple', width=0.03, linestyle=':', length_includes_head=True, label='Output V')
axs[1, 1].plot([stat_res_x, stat_res_x], [0, stat_res_y], 'k--', alpha=0.3)
axs[1, 1].plot([0, stat_res_x], [stat_res_y, stat_res_y], 'k--', alpha=0.3)
axs[1, 1].set_title("4. Decomposição H e V")
axs[1, 1].set_xlim(-2, 2); axs[1, 1].set_ylim(-2, 2)
axs[1, 1].set_aspect('equal'); axs[1, 1].grid(True)
axs[1, 1].legend(fontsize='small', loc='upper right')

plt.tight_layout()
plt.show()