a = float(input('enter the first number: '))
b = float(input('enter th second number: '))
c = float(input('enter the second number: '))

if a > b and a > c:
  print(a,' is largest among the three numberds.')
elif b > a and b > c:
  print(b, 'is largest among the three numbers.')
else:
  print(c, 'is largest among the three numbers.')