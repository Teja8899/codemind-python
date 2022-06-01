n=int(input())
for i in range(1,n+1,1):
    t=int(input())
    r=1
    for k in range(t,0,-1):
        r=r*k
    print(r,end='
')
