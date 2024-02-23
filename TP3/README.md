# TP3

- ## **Marta Ribeiro, a95408**

- O objetivo desde programa é somar inteiros **apenas** quando o somador estiver 'on'.
Quando encontra o caracter '=' é impresso no terminal a soma total até ao momento.
- A função ``` somador ``` devolve dois valores: o total obtido até ao momento, e o estado do
somador (*True* se estiver ligado, *False* se desligado), para que de cada vez que é lida uma
nova linha, não se percam os valores.
- A expressão regular faz *match* com todas as *strings* necessárias (também permite números 
negativos), e depois são comparadas para obter o resultado correto.


- Como testar:
``` cat exemplo.txt | python3 tpc3.py ```