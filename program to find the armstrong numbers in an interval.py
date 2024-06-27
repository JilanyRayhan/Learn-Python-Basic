  num0 = input()
  step = num0.strip().split(' ')
  n1,n2 = map(int,step)
  store = 0
  for num in range(n1,n2 + 1):
    num = str(num)
    size = len(num)
    for index in num:
      int_index = int(index)
      expo = int_index ** size
      store = store + expo
    if store != int(num):
      store = 0
    else:
      print(store)
      store = 0
