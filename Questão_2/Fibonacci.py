"""Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente
definido no código;"""
print('*' * 50)
#Definição dos parametros necessários par a execução, sendo o primerio número recebido (inputado pelo usuario)
Lista = list()
Valor1Fibo = int(input('Qual valor deseja obter o Fibonacci: '))
#Por se tratar de uma sequência fibonacci o valor 2 recebe o primeiro valor +1 que é como se começa a sequência
Valor2Fibo = Valor1Fibo + 1
#Para evitar erros a lista com a sequência fibonacci completa recebe os primeiros valores aqui
Lista.append(Valor1Fibo)
Lista.append(Valor2Fibo)

#Exibo o primeiro e segundo valor e crio um contador para que os números sejam mostrados e calculados em breve no laço while
print(f'{Valor1Fibo}→{Valor2Fibo}', end='→')
Contador = 3
#Realizo todo o calculo dentro do laço e recebo todos os valores calculados
while Contador <= 10:
    Calculo = Valor1Fibo + Valor2Fibo
    print(f'{Calculo}', end='→')
    Lista.append(Calculo)
    Valor1Fibo = Valor2Fibo
    Valor2Fibo = Calculo
    Contador += 1
#Este printe serve apenas para separar o laço do print abaixo
print()

#Não sabia se o núemro deveria ser inputado antes ou depois da sequência fibonacci ter sido exibida então coloquei-o aqui
NumeroPertencente = int(input('Digite um número para verificar se ele pertence a sequência Fibonacci: '))


#Verifico se o número pertence ou não a sequência se sim exibo o primeiro print do contrario exibo o segundo e finalizo o programa.
if NumeroPertencente in Lista:
    print(f'O valor digitado "{NumeroPertencente}" está na sequência')
else:
    print(f'O valor digitado "{NumeroPertencente}" não foi encontrado na sequência')
print('*' * 50)
