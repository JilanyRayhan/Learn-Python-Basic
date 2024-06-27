num = input().strip().split()
M,N = map(int,num)
product = M * N
if product >= 1 and product <= 256:
  dominos = product // 2
  print(dominos)