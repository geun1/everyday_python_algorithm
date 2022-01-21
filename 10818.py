import sys
num=int(input())
lst=input().split()
lt=[]
print(lst)
for i in lst:
    lt.append(int(i))

lt.sort()
print(lt[0],lt[-1])