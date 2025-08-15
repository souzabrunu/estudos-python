n1 = int(input('digite um valor:'))
n2 = int(input('digite outro:'))
s = n1 + n2
#print('A soma entre', n1, 'e', n2,'vale',s) 
#essa forma debaixo é uma forma mais usada
#atualmente e muito mais simples de etender.
print('A soma entre {} e {} vale {}'.format(n1,n2,s))
