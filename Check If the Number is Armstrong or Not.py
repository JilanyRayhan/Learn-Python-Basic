num = input()
store = 0
size = len(num)
for index in num:
  int_index = int(index)
  expo = int_index ** size
  store = store + expo

if store == int(num):
  print(num,"is an armstrong number.")
else:
  print(num,"isn't an armstrong number.")