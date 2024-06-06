secret_num='8'
guess=''
wanna_stop=False
guess_count=0
guess_limit=float('inf')


while guess != secret_num and not(wanna_stop):
  if guess_count<guess_limit and guess != 'q':
    guess=input('enter guess(between 1-10): ')
    guess_count += 1
    print(guess)
  else:
    wanna_stop=True

if wanna_stop:
  print('you are out of the game.')
else:
  print('your score is: 10')