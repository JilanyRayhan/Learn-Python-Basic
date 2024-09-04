import keyword

words = ["break","wonder","curtain","door","lambda","color","map","tiffin","ceiling","for"]

for i in range(len(words)):
  if keyword.iskeyword(words[i]):
    print(words[i], "is a keyword in python.")
  else:
    print(words[i],"not a keyword in python")