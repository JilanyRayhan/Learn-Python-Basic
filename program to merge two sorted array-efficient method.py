def merge_array(a,b):
  m,n = len(a),len(b)
  i,j = 0,0
  merged = []
  while i < m and j < n:
    if a[i] <= b[j]:
      merged.append(a[i])
      i += 1
    else:
      merged.append(b[j])
      j += 1

  while i < m:
    merged.append(a[i])
    i += 1
  while j < n:
    merged.append(b[j])
    j += 1
  return merged

n1 = [2,5,8,9,18]
n2 = [3,4,7,10,17,34]
merged_list = merge_array(n1,n2)
print(merged_list)