import random


print("hello. Welcome to the game!")


def menu():
    answer = input("Roll the dice?(y/n)").lower()
    if answer == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1},{dice2})')
    elif answer == 'n':
        print("Thanks for playing.")
    else:
        print("invalid answer!")


menu()
