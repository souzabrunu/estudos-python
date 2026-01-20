def lista_de_alunos():
    alunos = ['Bruno', 'Ana', 'Carol', 'Ricardo']

    # loop para garantir nome válido
    while True:
        novo_aluno = input('Digite o nome do novo aluno: ').capitalize()

        if not novo_aluno.isalpha():
            print('Nome inválido! Use apenas letras.')
        elif novo_aluno in alunos:
            print('Esse aluno já está na lista.')
        else:
            alunos.append(novo_aluno)
            break  # sai do loop quando estiver correto

    # loop para remover aluno
    while True:
        faltou = input('Digite o nome do aluno que faltou: ').capitalize()

        if faltou in alunos:
            alunos.remove(faltou)
            break
        else:
            print('Aluno não encontrado. Tente novamente.')

    print('Alunos presentes:', alunos)


lista_de_alunos()
