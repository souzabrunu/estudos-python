from time import sleep
n = int(input('Digite um número: '))
print('\nprocessando...\n')
sleep(2)
resultado = n % 2
if resultado == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é IMPAR'.format(n))

