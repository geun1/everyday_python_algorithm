num=int(input())
for i in range(1,num+1):
    print("*"*(i)+" "*(2*num-2*i)+"*"*(i))
for i in range(1,num):
    print("*"*(num-i)+" "*2*i+"*"*(num-i))