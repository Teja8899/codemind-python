a=input()
r=ord(input())
l=0
for k in range(0,len(a)):
    if r==ord(a[k]):
        l+=1
if l!=0:
    print(l)
else:
    print('-1')