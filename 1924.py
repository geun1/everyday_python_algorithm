import sys
a,b = map(int,sys.stdin.readline().split())
days=["SUN","MON","TUE","WED","THU","FRI","SAT"]
if a==1:
    num=b
elif a==2:
    num=b+31
elif a==3:
    num=b+59
elif a==4:
    num=b+90
elif a==5:
    num=b+120
elif a==6:
    num=b+151
elif a==7:
    num=b+181
elif a==8:
    num=b+212
elif a==9:
    num=b+243
elif a==10:
    num=b+273
elif a==11:
    num=b+304
elif a==12:
    num=b+334
print(days[num%7])