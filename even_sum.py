"""
Write a program to find the average of all even numbers in the given range.
if the strating range is Greater than ending range then print Invalid Range
"""
a=int(input())
b=int(input())
if(a<=0 or b<=0):
    print("Invalid Range")
else:
    c=0
    s=0
    if(a>b):
        t=a
        a=b
        b=t
    for i in range(a,b+1):
        if(i%2==0):
            c=c+1
            s+=i
    if(c!=0):
        print(s/c)
            
            
