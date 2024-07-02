import re
all_members = dir(re)
find_members = [member for member in all_members if "find" in member]
print(find_members)