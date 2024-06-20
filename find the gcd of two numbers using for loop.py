num1 = int(input('enter the first number: '))
num2 = int(input('enter the second number: '))
box = []
box1 = []
box2 = []
for i in range(2,int(num1/2)+1):
  if num1 % i == 0:
    box1.append(i)

for j in range(2,int(num2/2)+1):
  if num2 % j == 0:
    box2.append(j)

for element in box2:
  if element in box1:
    box.append(element)

if len(box) == 0:
  print('the two numbers have no common gcd.')
else:
  print('the gcd of the two numbers is:',box[-1])