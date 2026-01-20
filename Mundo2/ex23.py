peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('O seu imc é de {:.1f}'.format(imc))

if imc < 18.5:
    print ('Você esta ABAIXO do peso normal')
elif 18.5 <= imc < 25:
    print('Você está no peso normal')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA!')

 



