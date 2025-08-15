from random import randint
from time import sleep
computador = randint(0 , 5) # faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar

print('Processando...')
sleep(2)

if jogador == computador:
    print('Parabéns você ganhou')
else:
    print('Você errou eu pensei no número {} e não no {}'.format(computador,jogador))

    
