def task(fx,cue):
  return 6 + fx(cue)

def cube(x):
  return x ** 3

print(cube(2))
print(task(cube,5))