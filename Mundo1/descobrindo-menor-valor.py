a  = int(input('Digite um numero: '))
b  = int(input('Digite o segundo numero: '))
c  = int(input ('Digite o terceiro numero: '))

menor = a
#verificando qm é o menor
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
    #verificando qm é o maior
maior = a
if b>a and c>a:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))