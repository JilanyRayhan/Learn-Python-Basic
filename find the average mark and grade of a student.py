def find_avg_marks(marks):
  add = sum(marks)
  size = len(marks)
  avg = add/size
  return avg
def compute_grade(avg):
  if avg >= 80:
    print('your grade is: A+')
  elif avg >= 70 and avg < 80:
    print('your grade is: B')
  elif avg >= 60 and avg < 70:
    print('your grade is: C')
  else:
    print('you failed')

nums = input("enter the marks you obtained in 5 subjects: ").strip().split()
marks = [int(mark) for mark in nums]
avg = find_avg_marks(marks)
print("your average mark is:",avg)
grade = compute_grade(avg)