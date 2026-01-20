from time import sleep


def contagem_regressiva():
    for c in range(10, 0, -1):
        print(c)
        sleep(1)   # pausa 1 segundo

    print("FOGOOOOS 🎆")


contagem_regressiva()
