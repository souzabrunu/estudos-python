nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2 
print('A sua media foi {}'.format(media))

if media == 7.0:
    print('Você esta APROVADO!')
elif media > 7.0:
    print('Você esta APROVADO!')
if media >= 5.0 and media < 7.0:
    print('Você esta de RECUPERAÇÃO')
elif media < 5.0:
    print('Você esta REPROVADO!')

