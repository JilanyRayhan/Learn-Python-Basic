import operator
import time

list1 = [2,3,4]
list2 = [5,6,7]

t1 = time.time()
a,b,c = map(operator.mul,list1,list2)
t2 = time.time()

print("the value of a,b,c is: ",a,b,c)
print("total time taken to execute map is: ",t1 - t2)