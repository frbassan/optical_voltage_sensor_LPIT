import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

# --- 1. Parameters and Calculations ---
t = np.linspace(0, 2*np.pi, 200)
phi = np.pi/4  # 45-degree phase shift

# Sine waves
Ex_wave = np.sin(t)
Ey_wave = np.sin(t - phi)

# Base Vectors (Phasors)
vec_x = [0, 1]
vec_y = [np.sin(phi), np.cos(phi)]

# Static Sum (Phasorial)
stat_res_x = vec_x[0] + vec_y[0]
stat_res_y = vec_x[1] + vec_y[1]

# --- 2. Figure Configuration (2x2 Matrix) ---
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
plt.subplots_adjust(wspace=0.3, hspace=0.3)

# 1. Input Vector
axs[0, 0].arrow(0, 0, vec_x[0], vec_x[1], head_width=0.15, head_length=0.15, fc='red', ec='red', width=0.03, length_includes_head=True)
axs[0, 0].set_xlim(-2, 2); axs[0, 0].set_ylim(-2, 2)
axs[0, 0].set_title("1. Input Vector - after QWP (bias 90°)")
axs[0, 0].set_aspect('equal'); axs[0, 0].grid(True)

# 2. Sine Waves over Time (Limits: x: [0, 2pi], y: [-1, 1])
axs[0, 1].plot(t, Ex_wave, label='Ex', color='red')
axs[0, 1].plot(t, Ey_wave, label='Ey (Delayed)', color='green', linestyle='--')
axs[0, 1].set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
axs[0, 1].set_xticklabels([r'$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
axs[0, 1].set_xlim(0, 2*np.pi)
axs[0, 1].set_ylim(-1, 1)
axs[0, 1].set_title("2. Effect of LiNbO3 crystal (Pockels effect)")
axs[0, 1].legend(loc='upper right', fontsize='small'); axs[0, 1].grid(True)

# 3. Phasors and Sum (Limits [-2, 2])
axs[1, 0].arrow(0, 0, vec_x[0], vec_x[1], head_width=0.15, head_length=0.15, fc='red', ec='red', width=0.03, length_includes_head=True, label='Vector X')
axs[1, 0].arrow(0, 0, vec_y[0], vec_y[1], head_width=0.15, head_length=0.15, fc='green', ec='green', width=0.03, length_includes_head=True, label='Vector Y')
axs[1, 0].arrow(0, 0, stat_res_x, stat_res_y, head_width=0.15, head_length=0.15, fc='blue', ec='blue', width=0.03, linestyle='--', length_includes_head=True, label='Static Sum')
# Parallelogram lines
axs[1, 0].plot([vec_x[0], stat_res_x], [vec_x[1], stat_res_y], 'k--', alpha=0.3)
axs[1, 0].plot([vec_y[0], stat_res_x], [vec_y[1], stat_res_y], 'k--', alpha=0.3)
axs[1, 0].set_xlim(-2, 2); axs[1, 0].set_ylim(-2, 2)
axs[1, 0].set_aspect('equal'); axs[1, 0].grid(True)
axs[1, 0].set_title("3. Sum LiNbO3 crystal output (Pockels effect)")
axs[1, 0].legend(fontsize='small', loc='upper left')

# 4. Beam Splitter Effect (Limits [-2, 2])
axs[1, 1].arrow(0, 0, stat_res_x, stat_res_y, head_width=0.15, fc='blue', ec='blue', width=0.03, length_includes_head=True, label='Input (Sum)')
axs[1, 1].arrow(0, 0, stat_res_x, 0, head_width=0.15, fc='black', ec='black', width=0.03, linestyle=':', length_includes_head=True, label='Output H (X)')
axs[1, 1].arrow(0, 0, 0, stat_res_y, head_width=0.15, fc='purple', ec='purple', width=0.03, linestyle=':', length_includes_head=True, label='Output V (Y)')
axs[1, 1].plot([stat_res_x, stat_res_x], [0, stat_res_y], 'k--', alpha=0.3)
axs[1, 1].plot([0, stat_res_x], [stat_res_y, stat_res_y], 'k--', alpha=0.3)
axs[1, 1].set_title("4. Sum vector is split into H and V components (Pockels effect)")
axs[1, 1].set_xlim(-2, 2); axs[1, 1].set_ylim(-2, 2)
axs[1, 1].set_aspect('equal'); axs[1, 1].grid(True)
axs[1, 1].legend(fontsize='small', loc='upper left')

plt.tight_layout()
plt.show()