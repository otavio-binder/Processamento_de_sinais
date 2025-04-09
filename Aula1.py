#O que é um sinal->
"""
Sinal é uma função matemática que descreve um sistema biológico, físico ou químico, onde pode ser extraido informação

Eficaz vs Eficiente
Eficaz: que faz o objetivo, que consegue concluir objetivo com qualidade.
Eficente: Eficiencia está realcionado ao custo-benefício.

x[n] = xc(n*Ts)
"""

#Sinais em domínio contínuo ou discreto
#->DISCRETO: PODE resultar da amostragem de um sinal em domínio contínuo
#Exemplo de sinal
import numpy as np
import matplotlib.pyplot as plt

# Definindo parâmetros do sinal contínuo
t = np.linspace(0, 1, 1000)  # Tempo de 0 a 1 segundo, com 1000 pontos
f = 5  # Frequência do sinal em Hz
sinal_continuo = np.sin(2 * np.pi * f * t)  # Sinal senoidal de frequência f

# Amostragem do sinal contínuo
num_pontos = 15
t_discreto = np.linspace(0, 1, num_pontos)  # Pega 15 pontos uniformemente distribuídos no tempo
sinal_discretizado = np.sin(2 * np.pi * f * t_discreto)  # Avalia a função seno nesses pontos

# Criando a figura com subplots
fig, axs = plt.subplots(2, 1, figsize=(15, 9))

# Sinal contínuo + discreto
axs[0].plot(t, sinal_continuo, label='Sinal Contínuo')
axs[0].stem(t_discreto, sinal_discretizado, linefmt='r-', markerfmt='ro', basefmt='k', label='Amostras')
axs[0].set_title('Sinal Contínuo e Discreto')
axs[0].set_xlabel('Tempo (s)')
axs[0].set_ylabel('Amplitude')
axs[0].grid(True)
axs[0].legend()

# Apenas o sinal discretizado
axs[1].stem(t_discreto, sinal_discretizado, linefmt='r-', markerfmt='ro', basefmt='k', label='Sinal Discreto')
axs[1].set_title('Sinal Discreto')
axs[1].set_xlabel('Tempo (s)')
axs[1].set_ylabel('Amplitude')
axs[1].grid(True)
axs[1].legend()

# Ajustar espaçamento entre os gráficos
plt.subplots_adjust(hspace=0.4)

# Mostrar gráfico
plt.show()


#EQUAÇÃO DA AMOSTRAGEM A UMA TAXA CONSTANTE fs = 1/Ts
#--> x[n] = xc(n*Ts)