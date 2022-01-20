txt=input()
num=1
for i in range(len(txt)//10+1):
    
    if (i-1)==len(txt)//10:
        print(txt[num-1:])
    else:
        print(txt[num-1:num+9])
    num+=10