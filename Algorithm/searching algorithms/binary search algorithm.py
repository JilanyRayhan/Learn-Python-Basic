def binary(arr,target):
  left,right = 0,len(arr)-1
  while left <= right:
    mid = (left+right) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1

list1 = [10,20,30,40,50,60,70,80,90,100,110,120,130]
tar = 80
l = binary(list1,tar)
print(l)