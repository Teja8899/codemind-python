a=input()
r=0
for k in range(0,len(a)):
    if(ord(a[k])>48 and ord(a[k])<=57):
        r+=int(a[k])
print(r)