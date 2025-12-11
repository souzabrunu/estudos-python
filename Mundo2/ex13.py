curso = 'Python'

print(curso.center(10, '#'))

print('.'.join(curso))  # Mais comun de usar

nome = '  BruNo  '

print(nome.lstrip())  # Remove os espacos da esquerda.
print(nome.rstrip())  # Remove espaços da direita.
print(nome.strip().upper())  # Decide deixar strip em todas
print(nome.strip().lower())  # para mostrar que pode ser feito juntando tb.
print(nome.strip().title())

menu = 'Python'
print(menu.center(10, '#'))
