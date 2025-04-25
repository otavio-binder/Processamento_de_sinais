import matplotlib.pyplot as plt

# Etapa 1: Definindo as distâncias (em cm × 10)
distancia = [0.1, 0.2 , 0.3 , 0.4 , 0.5]

# Etapa 2: Definindo os tempos medidos para cada distância
# (substitua pelos seus dados reais)
medidat1 = [0.118, 0.118, 0.116, 0.116, 0.116]
medidat2 = [0.248, 0.253, 0.251, 0.252]
medidat3 = [0.349, 0.391, 0.373, 0.388, 0.386]
medidat4 = [0.513, 0.539, 0.541, 0.528, 0.536]
medidat5 = [0.656, 0.676, 0.658, 0.683, 0.690]

# Etapa 3: Calculando as médias para cada tempo
medit1 = sum(medidat1) / len(medidat1)
medit2 = sum(medidat2) / len(medidat2)
medit3 = sum(medidat3) / len(medidat3)
medit4 = sum(medidat4) / len(medidat4)
medit5 = sum(medidat5) / len(medidat5)

# Calculando as velocidades médias
v1 = distancia[0] / medit1
v2 = distancia[1] / medit2
v3 = distancia[2] / medit3
v4 = distancia[3] / medit4
v5 = distancia[4] / medit5

# Listas com resultados
medias = [medit1, medit2, medit3, medit4, medit5]
velocidades = [v1, v2, v3, v4, v5]

# Mostrando no console
print(f"Médias dos tempos: {medias}")
print(f"Velocidades médias: {velocidades}")

# Etapa 4: Gráfico do tempo médio x distância
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)  # 1 linha, 2 colunas, 1ª posição
plt.plot(distancia, medias, marker='o', linestyle='-', color='blue', label='Tempo médio')
plt.title('Tempo médio x Distância')
plt.xlabel('Distância m  ')
plt.ylabel('Tempo médio (s)')
plt.grid(True)
plt.legend()

# Etapa 5: Gráfico da velocidade média x distância (no mesmo gráfico)
plt.subplot(1, 2, 2)  # 1 linha, 2 colunas, 2ª posição
plt.plot(distancia, velocidades, marker='s', linestyle='--', color='green', label='Velocidade média')
plt.title('Velocidade média x Distância')
plt.xlabel('Distância m ')
plt.ylabel('Velocidade média m/s')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
