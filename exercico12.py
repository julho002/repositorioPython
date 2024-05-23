#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
#mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#°Salário Bruto até 900 (inclusive) - isento
#°Salário Bruto até 1500 (inclusive) - desconto de 5%
#°Salário Bruto até 2500 (inclusive) - desconto de 10%
#°Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
#No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#       Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00

hora_trabalhada=float(input('Insira a quantidade de horas trabalhada no mês:'))
valor_hora=float(input('Insira o valor da sua hora trabalhada:'))
salario_mes=hora_trabalhada *valor_hora

IR=(5/100)
FGTS=salario_mes*(11/100)
INSS=salario_mes*(10/100)
print('.....................................')
if salario_mes <=900:
    IR=0/100
    salario_mes=salario_mes-INSS
elif salario_mes <= 1500:
    salario_mes=salario_mes-IR
    salario_mes=salario_mes-INSS
elif salario_mes <= 2500:
    IR=10/100
    salario_mes = salario_mes - IR
    salario_mes = salario_mes - INSS
else:
    IR=20/100
    salario_mes = salario_mes - IR
    salario_mes = salario_mes - INSS

total_desconto=salario_mes-INSS-IR
salario_liquido=salario_mes-total_desconto

print('...........Salário Bruto:',salario_mes, '...........')
print('....................(-) INSS (10%)')
print(':', INSS)
print('........................FGTS (11%)')
print(':', FGTS)
print('................Total de descontos')
print(':', total_desconto)
print('...................Salário Liquido')
print(':', salario_liquido)