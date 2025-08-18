
print('-='* 20)
print('Analisador de Triângulos')
print('-='* 20)

r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Seguintos acima podem formar triangulo!')
else:
    print('Os seguimentos acima não podem formar Triângulo!')

