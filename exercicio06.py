#Faça um Programa que leia três números e mostre o maior deles.

num1 = input('digite o primeiro número:')
num2 = input('digite o segundo número:')
num3 = input('digite o terceiro número:')

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if(num1 > num2 and num1>num3):
    print('O número',num1,'é o maior')

elif(num2 > num1 and num2 > num3):
    print('O número',num2,'é o maior')

elif(num3 > num2 or num3 > num1):
    print('O número',num3,'é o maior')
else:
    print('Os números são iguais ou dois ou mais números são iguais.')
#código melhorado
try:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    num3 = int(input('Digite o terceiro número: '))

    if num1 == num2 == num3:
        print('Todos os números são iguais:', num1)
    else:
        maior_numero = max(num1, num2, num3)
        print('O número', maior_numero, 'é o maior.')

except ValueError:
    print('Por favor, insira apenas números inteiros.')
