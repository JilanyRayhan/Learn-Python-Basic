secret_word='cat'
guess=''
guess_count=0
guess_limit=3
guess_limit_exceeded=False

while guess != secret_word and guess_limit_exceeded==False:
  if guess_count<guess_limit:
    guess=input('guess an animal name containing 3 letters: ')
    guess_count += 1
  else:
    guess_limit_exceeded=True

if guess_limit_exceeded==True:
  print('you lost the game.')
else:
  print('you won.')