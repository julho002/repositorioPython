#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o
# programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#   °salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#   °salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#   °salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#   °o salário antes do reajuste;
#   °o percentual de aumento aplicado;
#   °o valor do aumento;
#   °o novo salário, após o aumento.

salario = float(input('Digite seu salário atual:'))

if salario <= 279:
    primeiro_aumento = salario *(20/100)
    salario_novo=primeiro_aumento+salario
    valor_aumento=salario_novo-salario
    print('RESUMO:');
    print('Salário antes do reajuste:',salario)
    print('Percentual de aumento aplicado:20%')
    print('valor do aumento:',valor_aumento)
    print('Novo salário após o aumento:',salario_novo)


if salario >= 280 and salario <=699:
    primeiro_aumento = salario *(15/100)
    salario_novo=primeiro_aumento+salario
    valor_aumento=salario_novo-salario
    print('RESUMO:');
    print('Salário antes do reajuste:',salario)
    print('Percentual de aumento aplicado:15%')
    print('valor do aumento:',valor_aumento)
    print('Novo salário após o aumento:',salario_novo)

if salario >= 700 and salario <=1499:
    primeiro_aumento=salario*(10/100)
    salario_novo=primeiro_aumento+salario
    valor_aumento=salario_novo-salario
    print('RESUMO:')
    print('Salário antes do reajuste:',salario)
    print('Percentual de aumento aplicado:10%')
    print('valor do aumento:',valor_aumento)
    print('Novo salário após o aumento:',salario_novo)

if salario >= 1500:
    primeiro_aumento=salario*(5/100)
    salario_novo=primeiro_aumento+salario
    valor_aumento=salario_novo-salario
    print('RESUMO:')
    print('Salário antes do reajuste:',salario)
    print('Percentual de aumento aplicado:5%')
    print('valor do aumento:',valor_aumento)
    print('Novo salário após o aumento:',salario_novo)

#codigo melhorado

salario = float(input('Digite seu salário atual: '))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100)
salario_novo = salario + aumento

print('RESUMO:')
print('Salário antes do reajuste: R$', salario)
print('Percentual de aumento aplicado:', percentual, '%')
print('Valor do aumento: R$', aumento)
print('Novo salário após o aumento: R$', salario_novo)
