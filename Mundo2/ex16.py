num = int(input('Escolha um numero inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] conversão para BINÁRIO
[2] conversão para OCTAL
[3] conversão para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{}  convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} conveertidoo para HEXADECIMAL é a {}'.format(num, hex(num)[2:]))
else:
    print('Opcão iinvalida, tente novamente')
