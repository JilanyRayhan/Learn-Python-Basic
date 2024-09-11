class FantasticFive:
  def __init__(self):
    self.num = 1

  def __iter__(self):
    return self

  def __next__(self):
    if self.num <= 5:
      value = self.num
      self.num += 1
      return value
    else:
      raise StopIteration

iterator = FantasticFive()
for number in iterator:
  print(number)