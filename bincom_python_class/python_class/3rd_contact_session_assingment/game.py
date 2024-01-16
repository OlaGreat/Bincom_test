import time

from datetime import date


print(date.today())
current_Time = time.localtime()
print(time.strftime("%H:%M:%S", time.localtime()))

f = time.strftime("%H:%M:%S", current_Time)
print(f)