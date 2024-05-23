#Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1=int(input('Digite um valor:'))
num2=int(input('Digite um segundo valor:'))
num3=int(input('Digite um terceiro valor:'))

lista_numeros = [num1,num2,num3]
lista_numeros.sort(reverse=True)
print(lista_numeros)

#Codigo melhorado

