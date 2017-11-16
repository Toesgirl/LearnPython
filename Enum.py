from enum import Enum,unique
Month=Enum('Month',('Jan','Feb','Mar','Apr'))
for name,member in Month.__members__.items():
    print(name,'=>',member,'.',member.value)


@unique
class weekday(Enum):
    sun=0
    mon=1
    tue=2
    wed=3
    thu=4
day1=weekday.mon
print(day1)
print(weekday.tue)
print(weekday['tue'])
print(weekday(1))
print(weekday.tue.value)
for name,member in Month.__members__.items():
    print(name,'=>',member)