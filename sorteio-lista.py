from random import choice
n1 = float(input('Primeiro N⁰: '))
n2 = float(input('Segundo N⁰: '))
n3 = float(input('Terceiro N⁰: '))
n4 = float(input('Quarto N⁰: '))
n5 = float(input('Quinto N⁰: '))
lifloata = [n1,n2,n3,n4,n5]
escolhido = choice (lifloata)
print('O N⁰ escolhido foi {:.0f}'.format(escolhido))

