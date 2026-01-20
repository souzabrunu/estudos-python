import bisect


def busca_rapida(nome, lista):

    lista.sort()  # busca binária exige lista ordenada

    index = bisect.bisect_left(lista, nome)

    if index < len(lista) and lista[index] == nome:
        return f'{nome} está na lista.'
    else:
        return f'{nome} não está na lista.'


alunos = ['Carlos', 'Ana', 'Bruno', 'Diana', 'Eduardo']

print(busca_rapida('Diana', alunos))
