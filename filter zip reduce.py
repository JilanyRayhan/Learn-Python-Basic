scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
pas = list(filter(lambda x: x > 75,scores))
print(pas)


dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
rev_drome = list(map(lambda x: x[::-1],dromes))
zipped = list(zip(dromes,rev_drome))
pdromes = list(filter(lambda x: x[0] == x[1], zipped))
print(pdromes)


new_pdromes = list(filter(lambda x: x == x[::-1],dromes))
print(new_pdromes)

from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]
addition = reduce(lambda x,y: x + y,numbers)
print(addition)

cng_initial = reduce(lambda x,y: x + y,numbers,10)
print(cng_initial)