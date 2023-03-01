"""4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro
do valor total mensal da distribuidora."""

#ATENÇÃO!! NÃO COMPREENDI EXATAMENTE O QUE FAZER NESTE EXERCICIO ENTÃO ESTE CÓDIGO FOI FEITO EM CONJUNTO COM UM AMIGO (SOMENTE ESTE DO EXERCICIO DE Nº 4)

#Criação do dicionario com todos os valores por estado
FaturamentoEstados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

#Soma de todos os valores dentro de suas prórpias regiões por exemplo: VALOR DE SP + VALOR DE RJ
ValorTotal = sum(FaturamentoEstados.values())

#Laço for de faturamento por estado (Para faturamento em itens dentro de faturamento por estado faça: o calculo abaixo) e por fim o print com o resultado
for Estado, Faturamento in FaturamentoEstados.items():
    Percentual = (Faturamento / ValorTotal) * 100
    print(f"{Estado}: {Percentual:.2f}%")
