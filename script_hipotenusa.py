#!/usr/bin/env python3

import sys #Importando o módulo sys

primeiro_lado = sys.argv[1] 
segundo_lado = sys.argv[2]
#Nesse bloco, foram criadas as variáveis para os lados do triângulo, os quais serão inseridos pelo usuário na linha de comando.

if not (primeiro_lado.isdigit() and segundo_lado.isdigit()): 
    print("Os números devem ser inteiros.") # Aqui será conferido se os valores fornecidos pelo usuário são números inteiros. Caso não sejam, será exibida a mensagem "Os números devem ser inteiros.".
else:
    primeiro_lado = int(primeiro_lado)
    segundo_lado = int(segundo_lado)
    # Essas duas linhas transformam o tipo das variáveis primeiro_lado e segundo_lado em integer.
    if primeiro_lado > 500 or segundo_lado > 500:
        print("Os números devem ser menores que 500.") # Aqui, o código verifica se os valores fornecidos são maiores que 500. Caso sejam, é mostrada a mensagem "Os números devem ser menores que 500."
    else:
        quadrado_da_hipotenusa = primeiro_lado**2 + segundo_lado**2
        print(f"O quadrado da hipotenusa para o triangulo retângulo com lados a= {primeiro_lado} e b= {segundo_lado}, é {quadrado_da_hipotenusa}") 
        #Caso os números fornecidos cumpram os requisitos anteriores (São inteiros e menores que 500), o código calcula o quadrado deles e os soma, armazenando o resultado na variável quadrado_da_hipotenusa. Após isso, imprime a mensagem informando o valor do quadrado da hipotenusa.