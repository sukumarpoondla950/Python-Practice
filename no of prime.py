#To find first N prime numbers in python
a=int(input())
if(a<=0):
    print("Invalid Input")
else:
    s=2
    c=0
    while(a>c):
        b=True
        for i in range(2,s):
            if(s%i==0):
                b=False
        if(b):
            print(s)
            c=c+1
        s=s+1
                
            
