secret_word="horse"
guess=''
i=1

while guess != secret_word and i<=3:
  guess=input ('Enter guess: ')
  i+=1
  if guess==secret_word:
    print('you won.')
  elif i>3:
    print('out of guesses. you lose!')