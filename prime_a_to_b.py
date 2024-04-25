#Write a program to print All the Prime Numbers between the Given Range.
a=int(input())
b=int(input())
if(a<=0 or b<=0):
    print("Invalid Input")
else:
    if(a>b):
        t=a
        a=b
        b=t
    for i in range(a,b+1):
        c=True
        if(a!=1 or b!=0):
            for j in range(2,i):
                if(i%j==0):
                    c=False
                    break
            if(c):
                print(i)
            
        
        
