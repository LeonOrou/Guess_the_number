import random
import time
print("I am thinking of a number between 1 and 20.")


def guessing():
    print("Take a guess o.O")
    global guess
    while not guessed:
        try:
            guess = int(input())
            if 1 < guess < 21:
                break
        except ValueError or TypeError:
            print('Please enter a valid number')
    if guess == num:
        print(f'Congratulations, you guessed the number "{num}" in {count} trys!')
        player_won()
    elif guess < num:
        print('Your number is too low')
    elif guess > num:
        print('Your number is too high')


def player_won():
    print('Play again? [y] or [n]')
    play_again = input()
    if play_again == 'y':
        global count
        global guess
        count = 0
        guess = 0
        print("I am thinking of a number between 1 and 20.")
    elif play_again == 'n':
        print('Thank you for playing!')
        time.sleep(3)
        exit()


guessed = False
count = 0  # trys of user
num = random.randint(1, 21)
while not guessed:
    guess = 0
    count += 1
    guessed = False
    guessing()
