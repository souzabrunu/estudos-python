
# utilizando função built-in range
for numero in range (0, 71, 7):
 print(numero, end='')

# utilizan um iterável
texto = input('Informe un texto:')
vogais = 'AEIOU'

for letra in texto:
    if letra.upper() in vogais:
       print(letra, end='')

