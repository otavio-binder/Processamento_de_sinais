#Teorema de Whittaker-Shammon

'''
Note que, se a amostragem a uma taxa de fs permite "adquirir"(medir) um sinal sem perda
de informação, pode ser possível calcular o sinal original em qualquer ponto teoricamente sem erro

Poderia ser que o processo de reconstrução fosse muito complexo, mas na verdade,
trata-se uma fórmula fechada se o critério de Nyquist for respeitado

Amostragem a uma taxa cte:

xc(t) ->  C/D -> x[n]
           |
           fs

Reconstrução:

x[n] -> D/C -> xr(t)
         |
         fs 

Fórmula de Shanon (ou formula de interpolação):

xr(t) = somatorio de n indo de -inf a inf
x[n] *sinc((t-n*Ts)/Ts), para todo t pertecente aos reais

sinc(x) = sen(pi*x)/(pi*x), se x != 0

obs: quando t coincide com m*Ts para algum m inteiro o resusltado da fórmula coincide com x[m]
quando t não é m*Ts para algum m inteiro, a fórmula não se reduz a x em um só ponto
'''