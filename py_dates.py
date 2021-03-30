import datetime

x = datetime.datetime.now()
print(x, type(x))
print(x.strftime('%A%a'))

# Create a date
x = datetime.datetime(2020,5,7)
print(x)