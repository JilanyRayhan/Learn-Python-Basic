def fact(num):
  if num == 0:
    return 1
  else:
    return num * fact(num-1)
a = int(input('enter a number here: '))
result = fact(a)
print('the factorial of the  given number is: ',result)