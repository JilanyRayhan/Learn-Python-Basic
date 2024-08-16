# solution 1
a = {1:"florida",2:"texas",4:"minnesota"}
b = {5:"rajbari",3:"dhaka",6:"rirozpur"}

print(b | a)
print({**a,**b})

# solution 2
c = {"florida": 4,"texas": 5,"minnesota": 6}
d = {"rajbari":1,"dhaka":2,"rirozpur": 3}

print({**c,**d})

# solution 3
e = {"florida": 4,"texas": 5,"minnesota": 6}
f = {"rajbari":1,"dhaka":2,"rirozpur": 3}

g = e.copy()
g.update(f)
print(g)