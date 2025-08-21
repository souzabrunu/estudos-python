s = float(input('Qual seu salario? '))
if s <= 1500:
        novo = s + ( s * 15 / 100 )
else:
        novo = s + ( s * 10 / 100 )
print('Seu salario com aumento ficou: R$:{:.2f}'.format(novo))



        

