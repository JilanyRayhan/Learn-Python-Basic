from datetime import datetime

date = "oct 3 1995 10:18AM"

t = datetime.strptime(date, "%b %d %Y %I:%M%p")
print(t)