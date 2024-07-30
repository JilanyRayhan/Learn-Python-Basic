  tup = (1,3,True,4,8,34,3,8,14)
  #A tuple with a single element requires a trailing comma
  tup1 = (1,)
  print(len(tup))
  print(type(tup))
  print(type(tup1))
  print(tup[1:5])
  rep = tup.count(3)
  ran = tup.index(8,5,8)
  print(rep)
  print(ran)

  #tuple is immutable, so in order to change, add or remove values from a tuple, at first, we convert the tuple into a list, then perform operations and finally convert it back to a tuple again
  country = ["brazil","nepal","vutan","sierra leone","germany"]
  country.append("maldives")
  country.append("srilanka")
  country[2] = "iran"
  country.pop(3)
  conv = tuple(country)
  recon = list[conv]
  print(type(recon))
  print(country)