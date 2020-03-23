import random
guesses_taken = 0

name = input("Hello! What is your name? ")
number = random.randint(1,20)

print('Well, ' + name + ', ' + 'I am thinking of a number between 1 and 20. Can you guess what it is?')
print('You have 3 tries.')

while guesses_taken <3 :
    guess = int(input('Take a guess: '))
    guesses_taken += 1
    if guess<number:
        print('Your guess is too low.')
    elif guess>number:
        print('Your guess is too high.')
    else:
        print('Congratulations! You guessed it!')
        break
else:
    print('Oh no! You have run out of tries. Better luck next time!')