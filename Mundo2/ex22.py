r1 = int(input('primeiro seguimento: '))
r2 = int(input('Segundo seguimento: '))
r3 = int(input('Terceito seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print ('Isósceles')
else:
    print('Os seguimentos acima não podem formar um triângulo!')
    


