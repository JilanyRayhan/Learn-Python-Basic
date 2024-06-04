a=int(input('enter the first number: '))
b=int(input('enter the second number: '))
c=int(input('enter the third number: '))

if a>b and a>c:
  print(str(a)+' is greater. ')
elif b>a and b>c:
  print(str(b)+' is greater. ')
elif c>a and c>b:
  print(str(c)+' is greater. ')
else:
  print('they all are equal.')