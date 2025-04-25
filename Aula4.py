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

#Representaçoes transformadas

'''
Vimos o conceito básico de cada um dos 4 cenário possíveis

Ficam 3 perguntas

1) Dado um conjunto de funçoes, como determinar se ele forma base?
.Dimensionalidade e independencia

2)Dado uma base, como calcular a transformada direta de um sinal, nessa base?

3)Para uma dada aplicaçao, como escolher um bom conjunto de funçoes para compor base?
.que base auxilia a enfatizar as informaçoes importantes para uma dada aplicaçao


Começaremos com as 2 primeiras questoes, com um exemplo em cada um dos cenários

e^(j*2*pi*f*t) = cos(2*pi*f*t) +  jsen(2*pi*f*t)

No contexto das transformadas de Fourier, as funçoes de base sao do tipo e^(j*2*pi*f*t),
onde f indica qual é a funçao de base e t é o ponto em que calcula a funçao.
Note que e^(j*2*pi*f*t) = cos(2*pi*f*t) +  jsen(2*pi*f*t), de forma que as funcoes
de base sao senoides complexas

Os valores de f a serem escolhidos para obter funções de base variam com o cenário (c1, c2, c3, c4) e, em alguns casos,
mesmo dentro do cenário. Os valores de t em que calculamos as funções também dependem do cenário.

Fourier -> sempre e^(j*2*pi*f*t)
.o que muda de um tipo para outro é a escolha particular de f e t

Exemplo:
    C1: Sinal em domínio discreto;
    Transformada em domínio discreto

x: {0, 1, 2 ,..., N-1} -> C
b_k: {0, 1, 2, ..., N-1}-> C

Queremos, neste exemplo, funções de base do tipo e^(j*2*pi*f*t)

Neste cenário, os valores de t (em e^(j*2*pi*f*t)) correspondem a variável discreta n,
que vai de nulo a N-1. Para f, precisamos de N valores, porque f identifica cada função de base,
e a dimensão dos sinais é N (precisamos de N funções de base).

Para escolhermos o f_s, obervamos o seguinte: uma vez que n é inteiro entre 0 e N-1, e e^(j*2*pi*f*t)
é periódica em f, com período 1. De fato: 

e^(j*2*pi*f*t)= cos(2*pi(f+1)n) +jsen(2*pi(f+1)n) = cos(2*pi*f*n) + jsen(2*pi*f*n)

Portanto, temos que escolher N frequências no intervalo de tamanho 1 em f. Escolheremos
frequências uniformemente espaçada em [0,1)

Então as frequencias serão

0, 1/N, 2/N, 3/N, ... até (N-1)/N, ou seja 

k/N, para tod k pertecente {0, 1, ..., N-1}

b_k[n] = e^((j*2*pi*k*n)/N), para todo k pertencente {0, 1, ..., N-1}

Para a transformada fracinária de Fourier
(FsFT)

b_k[n] = e^((j*2*pi*fr(k)*n)/N)

'''