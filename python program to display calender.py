import calendar

month = int(input("enter month: "))
year = int(input("enter Year: "))

cal = calendar.month(year,month)
print(cal)