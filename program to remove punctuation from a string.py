punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

sen = input("enter texts: ")
edited = ""

for i in sen:
  if i not in punc:
    edited = edited + i
print(edited)