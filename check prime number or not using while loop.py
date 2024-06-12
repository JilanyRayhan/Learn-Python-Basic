num = int(input('enter a number: '))
i = 2
while num >= 0 and num % i != 0 and i < num/2:
  if i > num/2:
    print(num, 'is a prime number.')
  i += 1
if num > 3 and num % i == 0:
  print(num, 'is a composite number.')
elif num == 0:
  print(num, 'is not a prime nor a composite.')
elif num == 1:
  print(num, 'is not a prime nor a composite.')
elif num < 0:
  print('a prime can\'t be negative.' )
else:
  print(num, 'is a prime number.')