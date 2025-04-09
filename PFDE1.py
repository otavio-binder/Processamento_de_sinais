import numpy as np
import matplotlib.pyplot as plt

# Dados reais das medições
trilha1 = [0.251, 0.613, 0.800, 0.900, 1.046, 1.233, 1.414, 1.654, 1.734, 2.039, 2.246, 2.538, 2.710, 2.922, 3.111]
trilha2 = [0.423, 0.799, 1.035, 1.413, 2.256, 3.142, 3.710]

# Eixos X
x1 = np.arange(1, len(trilha1) + 1)
x2 = np.arange(1, len(trilha2) + 1)

# Referência linear ideal (de 0 a 5 V) com o mesmo número de pontos
trilha1_ideal = np.linspace(0, 5, len(trilha1))
trilha2_ideal = np.linspace(0, 5, len(trilha2))

# Cálculo do EQM para cada trilha
eqm1 = np.mean((np.array(trilha1) - trilha1_ideal) ** 2)
eqm2 = np.mean((np.array(trilha2) - trilha2_ideal) ** 2)

# Criação dos gráficos
fig, axs = plt.subplots(2, 1, figsize=(13, 10))

# Trilha 1
axs[0].plot(x1, trilha1, marker='o', linestyle='-', label='Trilha 1 (medida)')
axs[0].plot(x1, trilha1_ideal, linestyle='--', color='gray', label='Trilha 1 (ideal)')
axs[0].set_xlabel("Pontos Medidos")
axs[0].set_ylabel("Tensão (V)")
axs[0].set_title(f"Medição de Tensão na Trilha 1 (EQM = {eqm1:.4f} V²)")
axs[0].set_ylim(0, 5)
axs[0].legend()
axs[0].grid(True)

# Trilha 2
axs[1].plot(x2, trilha2, marker='s', linestyle='-', label='Trilha 2 (medida)', color='orange')
axs[1].plot(x2, trilha2_ideal, linestyle='--', color='gray', label='Trilha 2 (ideal)')
axs[1].set_xlabel("Pontos Medidos")
axs[1].set_ylabel("Tensão (V)")
axs[1].set_title(f"Medição de Tensão na Trilha 2 (EQM = {eqm2:.4f} V²)")
axs[1].set_ylim(0, 5)
axs[1].legend()
axs[1].grid(True)

# Ajustar layout e exibir
plt.tight_layout()
plt.show()

# Exibir valores de EQM no console
print(f"Erro Quadrático Médio (Trilha 1): {eqm1:.4f} V²")
print(f"Erro Quadrático Médio (Trilha 2): {eqm2:.4f} V²")
