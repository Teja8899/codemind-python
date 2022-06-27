a=input()
r=0
for k in range(0,len(a)):
    if(ord(a[k])>=48 and ord(a[k])<=57):
        r+=1
if r!=0:
    print("Contains",r,"digit")
else:
    print("Doesn't contain digit")