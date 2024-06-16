data = ["sun",10,20,30,30,"moon",50,70,80,80,90]

def gro_dup(duplist):
  nodup_list = []
  for element in duplist:
    if element not in nodup_list:
      nodup_list.append(element)
  return nodup_list

print(gro_dup(data))