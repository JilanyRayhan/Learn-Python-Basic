import array
arr1 = array.array('i',[1,3,4,7,12,17,22])
arr2 = array.array('u',['a','b','d'])
arr3 = array.array('d',[1.944489,.8997987,3.87587])
print(len(arr3))

for i in range(0,len(arr1)):
  print(arr1[i],end=',')

num = list(range(0,100,10))
new_arr = array.array('i',num)
new_arr[9] = 100
new_arr.insert(3,12)
new = new_arr[1:6]
new2 = new[::-1]

#new_arr.pop(6)
#new_arr.remove("90")
print(new_arr)
print(new_arr[9])
print(new)
print(new2)


#print(dir(array))
a = array.array("i",[3,4,6,8,9])
b = a[2]
del a[3]
#for executind remove we directly put the element in the remove functioon instead of the index position
a.remove(6)
a.insert(1,5)
a.append(12)
print(a)
print(f"number of terms in the list: {len(a)}")


num = input("enter numbers:").strip().split()
num_list = [int(i) for i in num if int(i) > 0]
num_list.extend(a)
# extend not only takes another list and contains it wholly but also it can be used manually by adding values within a third bracket and extend it.
num_list.extend([3,5,23,656])
# if we keep the pop empty it will delete the last value of the array but upon puting a index position in  the pop, it will delete the specific index value
num_list.pop(10)
print(num_list)