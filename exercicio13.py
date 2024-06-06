#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

print('1-DOMINGO, 2-SEGUNDA-FEIRA, 3-TERÇA-FEITA, 4-QUARTA-FEITA, 5-QUINTA-FEIRA, 6-SEXTA-FEIRA, 7-SÁBADO')
dia_semana=int(input('DIGITE O NÚMERO CORRESPONDENTE AO DIA DA SEMANA:'))
if dia_semana == 1:
    print('HOJE É DOMINGO!')
elif dia_semana ==2:
    print('HOJE É SEGUNDA-FEIRA!')
elif dia_semana ==3:
    print('HOJE É TERÇA-FEIRA!')
elif dia_semana ==4:
    print('HOJE É QUARTA-FEIRA!')
elif dia_semana ==5:
    print('HOJE É QUINTA-FEIRA!')
elif dia_semana ==6:
    print('HOJE É SEXTA-FEIRA!')
elif dia_semana ==7:
    print('HOJE É SÁBADO!')
else:
    print('O NÚMERO É INVÁLIDO!')

#CÓDIGO MELHORADO
dias_semana = {
    1: "DOMINGO",
    2: "SEGUNDA-FEIRA",
    3: "TERÇA-FEIRA",
    4: "QUARTA-FEIRA",
    5: "QUINTA-FEIRA",
    6: "SEXTA-FEIRA",
    7: "SÁBADO"
}

dia_semana = int(input("DIGITE O NÚMERO CORRESPONDENTE AO DIA DA SEMANA: "))

if dia_semana in dias_semana:
    print(f"HOJE É {dias_semana[dia_semana]}!")
else:
    print("O NÚMERO É INVÁLIDO!")
