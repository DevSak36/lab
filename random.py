#random
import random

day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def dayguess():
        random_day = random.randint(0,len(day_of_week))
        print(random_day)
        day_goal = 0
        print(day_goal)
        
        while day_goal != random_day:
            day_goal = int(input(f'Guess a number between 1 and {x}: '))
            if guess < random_number:
                print('Sorry, guess again. Too low.')
            elif guess > random_number:
                print('Sorry, guess again. Too high.')

        print(f'Yay, congrats. You have guessed the number {random_number} correctly.')
        

#dayguess()



def guess(x):
    random_number = random.randint(1, x)
    print('hint: ' + str(random_number))
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
             print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly.')

#guess(10)


