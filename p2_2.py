from delorean import Delorean
from datetime import datetime, timedelta 

print("show UTC time: ")
d = Delorean()
d.truncate('second')
print(d)
print(d.datetime, d.date)

print("show Tokyo time: ")
d = d.shift("Asia/Tokyo")
d.truncate('second')
print(d)
print(d.datetime, d.date)

print("If people took plane from New York to Shanghai on special time, what time is it when he arrives Shanghai?") 
d1 = Delorean(datetime(2020, 3, 28,11,40), timezone='US/Pacific')
d1 = d1.shift("US/Eastern")
d1.truncate('minute')
print(d1)
d1 += timedelta(hours=15)
d1 = d1.shift("Asia/Shanghai")
print(d1)

print("What time is it on the last Tuesday in London")
d2 = Delorean()
print(d2.next_tuesday())





