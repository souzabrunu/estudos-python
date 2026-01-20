
data_nascimento = int(input('Digite sua data de nascimento: '))
idade = ( 2025 - data_nascimento)

print(3*'***==**') 
print('Sua idade é {} anos'.format(idade))

if idade >= 18:
    print('Você pode tirar sua CNH!')

elif idade == 17:
    print('Você já pode dar entrada na sua CNH!')
    
else:
    print('Você não pode tirar sua CNH!')



