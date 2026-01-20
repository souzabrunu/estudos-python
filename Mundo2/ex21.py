from datetime import date
atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento
print( 5* '---------')
print('Seja vem vindo ao programa de categoria!')
print( 5* '---------')
print('O atleta tem {}'.format(idade))
if idade <= 9 :
    print('Classificação MIRIM')
elif idade <= 14:
    print('Classificação INFANTIL')
elif idade <= 19:
    print('Classificação JUNIOR')
elif idade <=25:
    print('Classificação SÊNIOR')
else:
    print('Classificação MASTER')
    