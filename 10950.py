import sys
a=int(input())
for i in range(a):
    num1,num2=map(int,sys.stdin.readline().split())
    print(num1+num2)