
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salario: '))
anos  = int(input('Quantos anos de finaciamento? '))
prestacao = casa / ( anos * 12)
minimo  = salario * ( 30 /100 )
print('Para pagar uma casa de R$: {:.2f} em {} anos'.format(casa,anos))
print('A prestacao será de R$: {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo APROVADO!')
else:
    print('Emprestimo NEGADO! A prestacao ultrapassa 30% do salario.')
