"""5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE: a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente
definida no código; b) Evite usar funções prontas, como, por exemplo, reverse;"""

String = str(input('Digite o texto a ser invertido: '))
for Letras in String:
    Char = String[::-1]
print(f'O texto "{String}" de forma invertida é "{Char}"')