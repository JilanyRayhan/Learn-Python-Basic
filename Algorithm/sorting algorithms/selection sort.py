def selection(arr):
  n = len(arr)
  for i in range(0,n-1):
    mini = 0
    for j in range(i+1,n):
      if arr[j] < arr[i]:
        mini = j
        arr[i],arr[mini] = arr[mini],arr[i]

list1 = [40,30,20,10,5,3]
p = insertion(list1)
print(list1)