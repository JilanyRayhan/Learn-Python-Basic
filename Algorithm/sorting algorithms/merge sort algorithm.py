def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  l_side = arr[:mid]
  r_side = arr[mid:]
  l_side = merge_sort(l_side)
  r_side = merge_sort(r_side)
  return merge(l_side,r_side)

def merge(left,right):
  new = []
  i,j = 0,0
  while len(left) > i and len(right) > j:
    if left[i] < right[j]:
      new.append(left[i])
      i += 1
    else:
      new.append(right[j])
      j += 1

  new.extend(left[i:])
  new.extend(right[j:])
  return new

list1 = [40,60,10,20,100,50,70,45,25,5,1]
list1 =merge_sort(list1)
print(list1)