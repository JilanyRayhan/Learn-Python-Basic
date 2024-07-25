def bubble(arr):
  n = len(arr)
  for i in range(0,n):
    swapped = False
    for j in range(0,n - i - 1):
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
        swapped = True
    if not swapped:
      break

array1 = [40,50,10,20,30,5]
c = bubble(array1)
print(array1)