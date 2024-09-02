  dic1 = {
    1 : "mango",
    2 : "banana",
    3 : "orange",
    4 : "pineapple",
    5 : "peach"
  }

  name = input("enter a name: ")

  try:
    num = int(name)
    if num in dic1.keys():
      print("number: present")
    else:
      print("absent")

  except valueError:
    if name in dic1.values():
      print("name: present")
    else:
      print("absent")