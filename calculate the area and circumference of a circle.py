import math
def circle(r):
  def area():
    return math.pi*r*r
  def circumference():
    return 2*math.pi*r
  return area(), circumference()

radius = float(input('enter the radius of the circle: '))
area, circumference = circle(radius)
print('the area of the circle is: ',area)
print('the circumference of the circle is: ',circumference)