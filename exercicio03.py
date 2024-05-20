#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

feminino = 'F','f'
masculino='M','m'
print('Entre com uma letra M ou m(masculino) ou F ou f (feminino)')
sexo=input('Digite uma letra:')
if (sexo == 'M'):
    print('MASCULINO')
elif (sexo=='m'):
    print('MASCULINO')
elif(sexo == 'F' ):
    print('FEMININO')
elif(sexo == 'f' ):
    print('FEMININO')
else:
    print('SEXO INVALIDO')

#sexo = str(input('Digite (F)-Feminino, (M)-Masculino: ').upper())
#if sexo == 'M':
#    print('Sexo Masculino.')
#elif sexo == 'F':
#    print('Sexo Feminino.')
#else:
#    print('Sexo Inválido.')