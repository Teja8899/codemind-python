a=int(input())
b=int(input())
for i in range(a,b+1,1):
    m=0
    for j in range(1,i+1,1):
        if i%j==0:
            m+=1
    if m==2:
        print(i)