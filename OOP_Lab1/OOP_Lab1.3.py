import math
Time = list(input().split())
pay = 0
timein = int(Time[0]) * 60 + int(Time[1])
timeout = int(Time[2]) * 60 + int(Time[3])
totalTime = int(timeout) - int(timein)
if totalTime <= 15:
    pay = 0
elif totalTime <= 3*60:
    pay = math.ceil(totalTime/60)*10
elif totalTime <= 6*60:
    totalTime = totalTime - (3*60)
    pay = math.ceil(totalTime/60)*20 + 30
elif totalTime > 6 *60:
    pay = 200
print(pay)