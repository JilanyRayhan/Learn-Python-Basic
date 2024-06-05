n1=float(input('Enter the first number: '))
oprtr=(input('Enter the operator(+,-,*,/): '))
n2=float(input('Enter the second number: '))

if oprtr=='+':
  print(n1+n2)
elif oprtr=='-':
  print(n1-n2)
elif oprtr=='*':
    print(n1*n2)
elif oprtr=='/':
  print(n1/n2)
else:
  print('invalid operator.')