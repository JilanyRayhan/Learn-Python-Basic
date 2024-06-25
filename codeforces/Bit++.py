n = int(input())
store = 0
for i in range(n):
  case = input()
  if case == '++X' or case == 'X++':
    store = store + 1
  elif case == '--X' or case == 'X--':
    store = store - 1
print(store)    