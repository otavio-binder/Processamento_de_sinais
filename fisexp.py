import statistics
import matplotlib.pyplot as plt
import numpy as np

def calcular_media_desvio_padrao(medidas):
    if len(medidas) > 1:
        media = statistics.mean(medidas)
        desvio_padrao = statistics.stdev(medidas)
    elif len(medidas) == 1:
        media = medidas[0]
        desvio_padrao = 0  # Sem variação
    else:
        media = 0
        desvio_padrao = 0
    return media, desvio_padrao

# Dados
medidas_comprimento_regua = [4.9, 5.0, 4.7, 4.9, 4.8]
medidas_altura_regua = [2.6, 2.6, 2.8, 2.7, 2.7]
medidas_espessura_regua = [1.0, 1.2, 1.1, 1.1, 1.1]

medidas_comprimento_paquimetro = [5.06, 5.10, 5.09, 5.10, 5.10]
medidas_altura_paquimetro = [2.70, 2.70, 2.80, 2.80, 2.80]
medidas_espessura_paquimetro = [1.24, 1.28, 1.27, 1.28, 1.25]

medidas_furo = [2.0 , 2.0, 2.0, 2.0, 2.1]

volume = [330 -315, 330-315, 330-315, 330-315, 325-315]
# Cálculo para régua
mediac, desvio_padraoc = calcular_media_desvio_padrao(medidas_comprimento_regua)
mediaa, desvio_padraoa = calcular_media_desvio_padrao(medidas_altura_regua)
mediae, desvio_padraoe = calcular_media_desvio_padrao(medidas_espessura_regua)

# Cálculo para paquímetro
mediacp, desvio_padraocp = calcular_media_desvio_padrao(medidas_comprimento_paquimetro)
mediaap, desvio_padraoap = calcular_media_desvio_padrao(medidas_altura_paquimetro)
mediaep, desvio_padraoep = calcular_media_desvio_padrao(medidas_espessura_paquimetro)

#Calculo furo
mediaf, desvio_padraof = calcular_media_desvio_padrao(medidas_furo)

mediav, desvio_padraov = calcular_media_desvio_padrao(volume)
#Regua
print(f"Média comprimento regua: {mediac:.2f}")
print(f"Desvio padrão comprimento regua: {desvio_padraoc:.2f}")
print("Erro do comprimento: ", 0.05 + desvio_padraoc)
print(f"Média altura regua: {mediaa:.2f}")
print(f"Desvio padrão alutra regua: {desvio_padraoa:.2f}")
print("Erro da altura: ", 0.05 + desvio_padraoa)
print(f"Média espessura regua: {mediae:.2f}")
print(f"Desvio padrão espessura regua: {desvio_padraoe:.2f}")
print(f"Erro da espessura: ", 0.05 + desvio_padraoe ,"\n")

#Paquimetro
print(f"Média comprimento paquimetro: {mediacp:.2f}")
print(f"Desvio padrão comprimento paquimetro: {desvio_padraocp:.2f}")
print("Erro da comprimento: ", 0.05 + desvio_padraocp)
print(f"Média altura paquimetro: {mediaap:.2f}")
print(f"Desvio padrão alutra paquimetro: {desvio_padraoap:.2f}")
print("Erro da altura: ", 0.05 + desvio_padraoap)
print(f"Média espessura paquimetro: {mediaep:.2f}")
print(f"Desvio padrão espessura paquimetro: {desvio_padraoep:.2f}")
print("Erro da espessura: ", 0.05 + desvio_padraoep, "\n")

#Furo
print(f"Média diametro furo: {mediaf:.2f}")
print(f"Desvio padrão furo: {desvio_padraof:.2f}")

#volume
print(f"Média volume: {mediav:.2f}")
print(f"Desvio padrão volume: {desvio_padraov:.2f}")
# Criar gráficos
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Labels e dados
categorias = ['Régua', 'Paquímetro']
valores_comprimento = [mediac, mediacp]
valores_altura = [mediaa, mediaap]
valores_espessura = [mediae, mediaep]


desvios_comprimento = [desvio_padraoc, desvio_padraocp]
desvios_altura = [desvio_padraoa, desvio_padraoap]
desvios_espessura = [desvio_padraoe, desvio_padraoep]

# Gráfico de Comprimento
axs[0].bar(categorias, valores_comprimento, yerr=desvios_comprimento, capsize=3, color=['green', 'orange',])
axs[0].set_title('Média e Desvio Padrão - Comprimento')
axs[0].set_ylabel('Comprimento (cm)')

# Gráfico de Altura
axs[1].bar(categorias, valores_altura, yerr=desvios_altura, capsize=3, color=['green', 'orange', ])
axs[1].set_title('Média e Desvio Padrão - Altura')
axs[1].set_ylabel('Altura (cm)')

# Gráfico de Espessura
axs[2].bar(categorias, valores_espessura, yerr=desvios_espessura, capsize=3, color=['green', 'orange',])
axs[2].set_title('Média e Desvio Padrão - Espessura')
axs[2].set_ylabel('Espessura (cm)')

# Ajuste de layout e exibição
plt.tight_layout()
plt.show()
