num = int(input("enter the number: "))
n_trm = int(input("enter the number of term till you want to raise: "))
expo = list(map(lambda x: pow(num,x),range(0,n_trm+1)))
for i in range(len(expo)):
  print(expo[i])