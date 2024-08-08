def DtoB(n):
  if n <= 1:
    return [n]
  else:
    return DtoB(int(n / 2)) + [n % 2]

n = int(input())
if n <= 0:
  print("enter positive number.")
else:
  bi = DtoB(n)
  print(''.join(map(str,bi)))