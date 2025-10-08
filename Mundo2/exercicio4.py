from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = str(input('Se você é homem digite H, se for mulher digite M: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade  < 18:
    saldo = 18 - idade
    print('Ainda faltam {} para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos atrás!'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
    


