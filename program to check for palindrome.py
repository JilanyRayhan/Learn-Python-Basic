name = input('enter a name to check: ')
reverse_name = name[::-1]

if reverse_name != name:
  print('its not a palindrome.')
else:
  print('congrats, its a palindrome.')