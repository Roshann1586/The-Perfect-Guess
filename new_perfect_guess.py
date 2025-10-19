import random

scores = []
rounds = 1


def guess_the_number():

    actual_number = random.randint(1,100)
    your_guess = int(input("Guess a number between 1 and 100: "))

    guess_count = 1

    while your_guess != actual_number:

        if your_guess > actual_number:
            print('Think of a lower number')

        else:
            print('Think of a higher number')
        your_guess = int(input("Guess a number between 1 and 100: "))
        guess_count += 1

    if your_guess == actual_number:
        print(f'You made it in {guess_count} guesses')

    scores.append(guess_count)
    play_or_not = input("Do you want to play again? (y/n): ")

    while play_or_not.lower() not in ['y', 'n']:
        print('Choose a valid option')
        play_or_not = input("Do you want to play again? (y/n): ")

    if play_or_not.lower() == 'y':
        global rounds
        rounds += 1
        guess_the_number()

    elif play_or_not.lower() == 'n':
        print(f'Best Score : {min(scores)}')
        print(f'Total rounds : {rounds}')
        scores.clear()

guess_the_number()