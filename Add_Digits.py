n=int(input())
a=0
while n:
    r=n%10
    a+=r
    n=n//10
    if n==0 and a>10:
        n=a
        a=0
print(a)
        
    