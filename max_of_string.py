a=input()
r=0
l=0
for k in range(0,len(a)):
    if r<ord(a[k]):
        r=ord(a[k])
        l=a[k]
print(l)