#2 paradigmas inicias data 04/04/2025


"""
Sinais em domínio contínuo --> processamento analógico em geral, circuito eletrônicos

Sinal original --> transdutro --> Sinal elétrico --> **circuito de processamento** --> Sinal elétrico processador --> atuador --> SINAL FINAL
                                                                 |
                                                        produção do circuito:
                                                        .projeto de processamento 
                                                        .instrumentação

Sinais em domínio discreto --> processamento digital
|
-> Sinal original --> transdutor --> digitalização --> SINAL DIGITAL --> processador --> sinal digital processado --> conversão D/A --> atuador --> SINAL FINAL

Digitalização --> quantização e amostragem --> conversor A/D típico faz os 2

Existem condições para as quais a amostragem x[w] = hc(n*Ts) não leva a perdas de informação. O exemplo mais conhecido (que não é único)
é o de um sinal cujo espectro é nulo fora do intervalo (-fm1 fm) e nesse caso, uma amostragem com fs >= 2fm preserva toda a informação do sinal
Trata-se do critério de Nuquist
"""