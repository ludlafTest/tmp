import random

def guess(z):
    random_number = random.randint(1, z)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number beteween 1 and {z}: '))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    
    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

def computer_guess(z):
    low = 1
    high = z
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


computer_guess(1000)