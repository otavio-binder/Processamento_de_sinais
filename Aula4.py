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

então:

xc(t) = somatorio de -inf a inf de
x[n]*sinc((t-n*Ts)/Ts) para todo t pertecente aos reais
Esta equaçao exige que o critério de Nyquiste tenha sido respeitado

'''

#Representações Transformada

'''
Conceito: uma transformada de um sinal é uma representação matemática em termos de pesos que devem mutliplicar
funções de base conhecidas (e especificadas), de forma que a soma ponderada (por esses pesos) dessas funçoes resulte no sinal original

Objetivo: evidenciar prorpriedade do sinal, a partir das propriedades das funções que já são conhecidas, uma vez que
soubermos quais têm mais peso na composição daquele sinal

#somatório ou integral

Note que há 4 cenários possíveis diante desse conceito:

C1-> Sinal em tempo discreto;
    Transformada em domínio discreto

C2-> Sinal em tempo discreto;
    Trasnformada em domínio contínuo

C3 -> Sinal em tempo contínuo;
    Transformada em domínio discreto

C4 -> Sinal em tempo contínuo;
     Transformada em domínio contínuo
'''

#Representações transformadas

'''
Para quê? -> Para analisarmos um sinal de interesse como soma ponderada de funções conhecidas

*transformada em si: os pesos nessa soma

*soma: somatório ou integral

C1:
obs: para o espaço do todos os sinias com domínio {0, 1, 2, ... , N-1} e contradomínio C,
temos dimensão N. Logo qualquer conjunto {b0, b1, b2,..., b_n-1} linearmente independente uma base

x[n] = somatorio de k= 0 a n-1 de
xchapeu[k] b_k[n] transformada inversa


C2: 

x: Z -> C
b_lambida: Z-> C, para todo lambida pertecente [a , b)


x[n] = integral de a a b de (xchapeu(lambida)*b_lambida[n]* dlambida)

C3:

x_c: [alpha, beta] -> C ou x_c: R -> C
b_k: [alpha, beta] -> C ou b_k: R -> C

para todo k pertecente a Z (por exemplo)

x_c(t) = somatorio de k = -inf a inf de
xchapeu_c[k] * b_k(t)   transformada inversa


C4:

x_c: R -> C
b_lambida: R-> C, para todo lambida pertecente R, 

x_c(t) = integral de -inf a inf de xchapeu_c(lambida)* b_lambida(t) * dlambida
'''