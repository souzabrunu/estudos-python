from random import randint


def play_game():

    secret_number = randint(1, 10)
    cont = 0

    while True:

        guess = int(input('What is your guess 1 by 5? '))

        cont += 1

        if guess > secret_number:
            print('Too high!!')
        elif guess < secret_number:
            print('Too low')
        elif guess == secret_number:
            print(f'you got it right in  {cont} attempts')
            break


play_game()
