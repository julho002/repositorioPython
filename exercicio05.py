#Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
not1=0
not2=0
not1 = int(input('Informe a primeira nota:'))
not2 = int(input('Informe a segunda nota:'))
med=(not1+not2)/2
if(not1 ==None):
    not1=0
if(not2== None):
    not2=0

if (med >7 and med<=9):
    print('APROVADO')
elif (med < 7):
    print('Reprovado')
elif(med >= 10):
    print('Aprovado com Distinção')