def rectangle_properties(len,wid):
  def area():
    return len * wid
  def perimeter():
    return 2 * (len + wid)

  return area(), perimeter()

a = float(input('enter length: '))
b = float(input('enter width: '))
area, perimeter = rectangle_properties(a,b)

print(area)
print(perimeter)
