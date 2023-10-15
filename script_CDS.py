#!/usr/bin/env python3

import sys

sequencia = sys.argv[1]
n1 = sys.argv[2]
n2 = sys.argv[3]
n3 = sys.argv[4]
n4 = sys.argv[5]
n5 = sys.argv[6]
n6 = sys.argv[7]

if not (sequencia.isalpha() and n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit() and n5.isdigit() and n6.isdigit()): 
    print("O primeiro argumento deve ser composto apenas por letras e os outros argumentos devem ser números inteiros.")
    # Aqui será conferido se os valores fornecidos pelo usuário para n1 a n6 são números inteiros e se a sequência de DNA é composta apenas por letras.
else:
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    n4 = int(n4)
    n5 = int(n5)
    n6 = int(n6)
    sequencia = sequencia.upper()
    # Caso os requisitos sejam cumpridos, os valores de n1 a n6 são convertidos para integer e todas as letras da sequência de DNA são transformadas em caixa alta para evitar confusões.

    if n1 > len(sequencia) or n2 > len(sequencia) or n3 > len(sequencia) or n4 > len(sequencia) or n5 > len(sequencia) or n6 > len(sequencia):
        print(f"Os números fornecidos não podem ser maiores que o tamanho da sequência de dna, que é {len(sequencia)}")
        # Essas duas linhas verificam se nenhum dos números fornecidos é maior que o comprimento da sequência de DNA.
    else:
        cds1 = sequencia[n1-1:n2]
        cds2 = sequencia[n3-1:n4]
        cds3 = sequencia[n5-1:n6]
        # Atribui-se às variáveis cds1, cds2 e cds3 os caracteres presentes nas posições de n1 a n2, n3 a n4 e n5 a n6 respectivamente.

        if cds1.startswith("ATG"):
            codon_de_inicio = True
        else:
            codon_de_inicio = False
        if cds3.endswith("TAG") or cds3.endswith("TAA") or cds3.endswith("TGA"):
            codon_de_parada = True
        else: 
            codon_de_parada = False
        # Essa parte do código verifica se a variável CDS 1 começa com o códon de início e, em seguida, se a variável CDS 3 termina com algum dos códigos de parada. Além disso, armazena os resultados dessas verificações em duas novas variáveis chamadas codon_de_inicio e codon_de_parada.

        if codon_de_inicio and codon_de_parada:
            print(cds1+cds2+cds3) 
        elif codon_de_inicio and not codon_de_parada:
            print("A sequência CDS 3 não termina com um dos possíveis códigos de parada.")
        elif codon_de_parada and not codon_de_inicio:
            print("A sequência CDS 1 não se inicia com o códon de início.")
        else:
            print("A sequência CDS 1 não se inicia com o códon de início e a sequência CDS 3 não termina com um dos possíveis códigos de parada.")
        # Por fim, o código verifica se as variáveis codon_de_inicio e codon_de_parada são verdadeiras e se forem, imprime na tela a junção de cds1, cds2 e cds3. Caso uma delas ou ambas não sejam verdadeiras, o código imprime na tela uma mensagem afirmando isso.