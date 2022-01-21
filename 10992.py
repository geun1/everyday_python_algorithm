num=int(input())
for i in range(1,num+1):
    if i == num:
        print("*"*(2*i-1))
    elif i == 1:
        print(" "*(num-1)+"*")    
    else:
        print(" "*(num-i)+"*"+" "*(2*i-3)+"*")
