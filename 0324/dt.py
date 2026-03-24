import datetime

# from datetime import datetime
# now = datetime.now()

now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

print(now.date())
print(now.time())
print(now.today())
print(now)

print(now.weekday())
print(now.isoweekday())
