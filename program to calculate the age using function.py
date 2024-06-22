from datetime import date
def calculate_age(birth_date):
  today = date.today()
  age = today.year - birth_date.year - ((today.month,today.day) < (birth_date.month,birth_date.day))
  return age

p = input('enter the birth date in yyyy-mm-dd format: ')
year,month,day = map(int,p.split('-'))
birth_date = date(year,month,day)
age = calculate_age(birth_date)
print('you are',age,'years old.')