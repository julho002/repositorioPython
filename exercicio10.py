#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino  ou V-Vespertino
# ou N- Noturno sendo que o usuario possa digitar M maiusculo ou minusculo bem como V maiusculo ou minusculo e N maiusculo ou minusculo
#. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",conforme o caso.

#turno=str(input('Digite M-Matutino, V-Vespetino ou N-Noturno:'))
#print(turno)

#if turno == 'M' and 'm':
    #print('BOM DIA!')
#if turno == 'V' and 'v':
    #print('BOA TARDE!')
#if turno == 'N' and 'n':
# print('BOA NOITE!')
#else:
#   print('Valor Inválido')

#codigo melhorado

turno=input('Digite M para Matutino, V para Vespertino ou N para Noturno:').upper()#A função .upper() é usada para converter a entrada do usuário em maiúsculas, permitindo que o programa compare facilmente a entrada do usuário com as opções válidas ('M', 'V', 'N')

if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')