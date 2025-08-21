d = float(input('Qual a distancia percorrida? '))
print('\nVocê fez uma viagem de {} km/h \n'.format(d))

if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45

print('O preço da sua viagem ficou R$: {:.2f}'.format(preço))