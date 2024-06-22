import datetime
p_date = input('enter the date in YYYY-MM-dd: ')
y1,m1,d1 = p_date.split('-')
y1 = int(y1)
m1 = int(m1)

c_date = datetime.datetime.now()
y2 = c_date.year
m2 = c_date.month

age = y2 - y1 
if m2 < m1:
    age -= 1
    m2 += 12

m = m2 - m1
print('your age is',age,'years',m,'months.')