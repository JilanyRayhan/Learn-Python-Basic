# trick 1

mark = 80
print("excellent work") if mark > 90 else print("good job")

# trick 2

num = 80
if num in [80,90,95]:
  print("good work")

# trick 3

l = [50,30,60,20,10,90]
a = [i * 2 for i in l if i < 90]
print(a)

# trick 4

for index,char in enumerate(l):
  print(f"{index} : {char}")

# trick 4 with a tuple form

for index in enumerate(l):
  print(index)

# trick 5 for separator

num1 = 90_00_000
num2 = 10_000

sum = num1 + num2
print(f"{sum:,}")

# trick 6 with lambda

b = lambda x: x*x #or x**2
print(b(5))

# trick 7 with zip

names = ["rahim","karim","jodu","modu"]
marks = [40,76,20,60]
subs = ["math","biology","physics","ict"]

for name,mark,sub in zip(names,marks,subs):
  print(name,"has scored",mark,"marks in", sub)

# trick 8 using shell
# from getpass import getpass
# username = input("enter username:")
# password = getpass("enter password:")

# trick 8

l = [10,20,30,40,50,80,10,20,30,12,17]
s = set(l)
p = list(s)
print(s)
print(p)

# trick 9 and 10

s_list = sorted(p, reverse = True)
print(s_list)

# trick 11 for sorted (dictionary within a list)

dl = [{"name" : "rahim", "age" : 40},
      {"name" : "karim", "age" : 20},
      {"name" : "jodu", "age" : 30},
      {"name" : "modu", "age" : 10}]

sorted_list = (sorted(dl,key = lambda x:x["name"]))
sorted_age = (sorted(dl,key = lambda x:x["age"]))
print(sorted_list)
print()
print(sorted_age)


