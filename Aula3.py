import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Efeito espectral da multiplicação de um sinal por um trem de impulsos
# ============================================================

# Sinal xc(t) com transformada de fourier xchapeuc(f) tendo suporte em [-fm;fm]
# Imagens abaixo

# Parâmetros do sinal
fs = 1000  # taxa de amostragem (Hz)
T = 1      # duração do sinal (s)
t = np.linspace(0, T, int(fs*T), endpoint=False)  # vetor de tempo
periodo = 0.1     # período do trem de impulsos (s)
N = int(fs * T)   # número total de amostras
n = np.arange(N)  # vetor de índices de tempo discreto

# Frequências dos componentes
f1 = 50   # Hz
f2 = 120  # Hz

# Criando o trem de impulsos
impulso = np.zeros(N)
impulso[::int(fs * periodo)] = 1  # coloca 1 a cada 'fs*periodo' amostras

# Vetor de tempo
timpulsos = n / fs

# Sinal contínuo amostrado xc(t)
xc_t = np.sin(np.pi*f1*t) + 4*np.sin(2*np.pi*f2*t)

# Multiplicando o sinal pelo trem de impulsos
xa_t = xc_t * impulso

# Transformada de Fourier (FFT) do sinal contínuo
X_f = np.fft.fft(xc_t)
# Transformada de Fourier (FFT) do sinal amostrado
Xa_f = np.fft.fft(xa_t)
f_eixo = np.fft.fftfreq(len(t), d=1/fs)  # eixo de frequência

# Apenas a parte positiva do espectro
mask = f_eixo >= 0

# Plotando o sinal no tempo (xc(t))
plt.figure()
plt.plot(t, xc_t)
plt.title('Sinal no tempo $x_c(t)$')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid(True)


# Plotando a transformada de Fourier de xc(t)
plt.figure()
plt.plot(f_eixo[mask], np.abs(X_f[mask]) * 2 / len(t))  # normalização
plt.title('Transformada de Fourier $\\hat{x}_c(f)$')
plt.xlabel('Frequência [Hz]')
plt.ylabel('Magnitude')
plt.grid(True)


# Plotando o trem de impulsos (i(t))
plt.figure()
plt.stem(timpulsos, impulso)  # se apresentar problema com use_line_collection, remova-o
plt.title('Trem de Impulsos')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Plotando o sinal amostrado (xa(t))
plt.figure()
plt.plot(t, xa_t, 'ro-')
plt.title('Sinal Amostrado $x_a(t) = x_c(t) \\cdot i(t)$')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Plotando a transformada de Fourier do sinal amostrado
plt.figure()
plt.plot(f_eixo[mask], np.abs(Xa_f[mask]) * 2 / len(t))  # normalização
plt.title('Transformada de Fourier do Sinal Amostrado $\\hat{x}_a(f)$')
plt.xlabel('Frequência [Hz]')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()

'''
Teorema de Nyquist: 
A T.F do sinal y(t) obtido pela multiplicação de um sinal arbitrário xc(t) (que admite T.F) 
pelo trem de impulsos i(t), com os impulsos afastados de TS é dada por

ychapeuc(f) = somatório de K de -infinito a infinito de
xchapeuc*(f-(K/Ts)),  para todo f pertecente aos reais

onde xchapeuc é T.F de xc
Interpretação: o resultado da multiplicação de um trem de impulsos por um sinal xc(que admite T.F) tem uma que é a 
soma infinitas de réplicas da T.F original, espaçadas de fs = 1/Ts

No caso em que o espaçamento do impulso é menor do que 1/2fm, as réplicas não se sobrepõem.

PORTANTO  Ts< 1/2fm
'''
