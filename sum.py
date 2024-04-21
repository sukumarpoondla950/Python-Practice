a=int(input())
b=int(input())
s=0
if(a>b):
    t=a
    a=b
    b=t
for i in range(a,b+1):
    s=s+i
print(s)
