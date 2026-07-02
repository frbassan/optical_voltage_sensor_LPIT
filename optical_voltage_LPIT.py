import numpy as np
import matplotlib.pyplot as plt

# Parâmetros Físicos
U_pi = 15000  # Tensão de meia-onda do cristal (15 kV)

# Ponto de operação central (Centro da faixa 10kV - 15kV)
U_center = 12500 

# Cálculo do Bias para centrar em 12.5 kV
# Queremos que S = sin(phi - bias) = 0 quando U = 12.5 kV
# bias = pi * (U_center / U_pi)
bias = np.pi * (U_center / U_pi)

# Faixa de simulação (0 a 20 kV para observar o comportamento fora da linearidade)
voltages = np.linspace(0, 20000, 400) 

# Cálculo da Fase e do Sinal Normalizado
phi = np.pi * (voltages / U_pi)
S = np.sin(phi - bias)

# Plotagem
plt.figure(figsize=(12, 6))
plt.plot(voltages/1000, S, label=r'$S = \sin(\pi \cdot \frac{U}{U_\pi} - bias)$', color='green', linewidth=2)

# Destacando a Região de Operação Linear (10kV a 15kV)
plt.axvspan(10, 15, color='yellow', alpha=0.3, label='Linear Operating Range (10-15kV)')

# Destacando o ponto central e eixos
plt.axvline(12.5, color='red', linestyle='--', label='Centered at 12.5kV')
plt.axhline(0, color='gray', linestyle=':', alpha=0.5)

# Detalhes do gráfico
plt.title('Voltage Sensor: Linear Operation Highlight (10kV - 15kV)')
plt.xlabel('Voltage (kV)')
plt.ylabel('Normalized Signal (S)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()