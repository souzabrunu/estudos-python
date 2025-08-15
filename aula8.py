n1 = int(input('Digite um valor: '))
n2 = int(input( 'Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# esse end= ''é para o código continuar na mesma linha mesmo tendo 2 prints.
# o :2.f é para pegar da divisao somente os 2 primeiro numeros.
print('A soma é {} o produto é {} e a divisao é {:.2f}' .format(s, m, d,), end= ' ')
print('Divisão inteira {} e potencia {}'.format(di, e))
