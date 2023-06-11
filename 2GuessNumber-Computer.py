import random

rand_num = random.randint(1,10)

user_num = int(input("Guess a number between 1 and 10: "))

while user_num != rand_num:
        if user_num < rand_num:
            print("""Sorry, guess again. Too low.""")
        else:
            print("""Sorry, guess again. Too high.""")
        user_num = int(input("Guess a number between 1 and 10: "))

if user_num == rand_num:
    print("""Yay, congrats. You have guessed the number {} correctly!!""".format(rand_num))