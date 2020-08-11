from datetime import date
# from datetime import time
# from datetime import datetime
'''The datetime classes in Python are categorized into main 5 classes.

date – Manipulate just date ( Month, day, year)
time – Time independent of the day (Hour, minute, second, microsecond)
datetime – Combination of time and date (Month, day, year, hour, second, microsecond)
timedelta— A duration of time used for manipulating dates
tzinfo— An abstract class for dealing with time zones
'''

#
# How to Use Date & DateTime Class
#
def main():
    today = date.today()
    print(type(today))
    print("Today's date is ",today)
    print('Date Components:',today.day,today.month,today.year ,today.weekday())


if __name__=='__main__':
    main()