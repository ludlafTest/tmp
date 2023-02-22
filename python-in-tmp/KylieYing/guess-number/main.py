import random

def guess(z):
    random_number = random.randint(1, z)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number bete¡ween 1 and {z}: '))
        if guess < random_number:
            print("Sorrys, guess again. Too low.")
        elif guess > random_number:
            print("sorry, guess again. Too high.")
    
    print(f'yay, congratulationes. You have guessed the number {random_number} correctly!')


guess(10)