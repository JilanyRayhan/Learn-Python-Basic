num = int(input('enter a number: '))

if num > 1:
  for i in range(2,int((num/2)+1)):
    if num % i == 0:
      print(num, 'is not prime.')
      break
  else:
    print(num, 'is prime')
elif num < 0:
  print(num, 'or any other negetive numbers can\'t be prime.')
else:
  print(num, 'is neither prime nor composite.')