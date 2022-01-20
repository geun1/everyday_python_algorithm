import sys
line = sys.stdin.readlines()
for i in line:
    a,b=map(int,i.split())
    print(a+b)