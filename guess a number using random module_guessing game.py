import random

low = 50
high = 100
guesses = 0

num = random.randint(low,high)

while True:
  guess = int(input(f'\n please enter a number between {low}-{high}: '))
  guesses += 1
  if guess > num:
    print('\n',guess, 'is larger.')
  elif guess < num:
    print('\n',guess, 'is smaller.')
  else:
    print('\n->congrats, you got it correct. the number is: ', num)
    break

print('you took', guesses, 'guessess.')