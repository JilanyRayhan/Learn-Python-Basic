num1 = int(input('enter the first number: '))
num2 = int(input('enter the second number: '))

a = max(num1,num2)
b = min(num1,num2)

while a % b != 0:
  c = a % b
  a = b
  b = c

print('the GCD of the two numbers is:',b)