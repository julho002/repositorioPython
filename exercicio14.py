#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao
# longo de um semestre,e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
# “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
primeira_nota= float(input('Digite o valor da Primeira Nota:'))
segunda_nota= float(input('Digite o valor da Segunda Nota: '))
media_nota=(primeira_nota + segunda_nota)/2
print('Média da nota:',media_nota)
if 9.0 <= media_nota <= 10.0:
    print('APROVADO \n A')
elif 7.5 <= media_nota <= 9.0:
    print('APROVADO \n B')
elif 6.0 <= media_nota <= 7.5:
    print('APROVADO \n C')
elif 4.0 <= media_nota <= 6.0:
    print('REPROVADO \n D')
elif 0.0<= media_nota <= 4.0:
    print('REPROVADO \n E')
else:
    print('valor deve ser inserido novamente!')