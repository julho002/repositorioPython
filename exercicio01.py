#Faça um Programa que peça dois números e imprima o maior deles.
x =0;
y =0;
i=0
while i < 2:
    x =input('Digite o primeiro número:');
    y= input('Digite o segundo número:');
    if (x>y):
        print('O primeiro número á maior:');
    elif (x<y):
        print('O segundo número é maior:');
    else:
        print('Os valores são iguais');

    print('--------------------------------------------')

    print('.',i)
    i+=1;