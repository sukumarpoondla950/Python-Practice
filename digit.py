"""Write a Program to Print Sum of all odd Positions in a Given Number?
If the Input is 5432 then print output as 6."""
a=int(input("Enter a Number:"))
if(a<=0):
    print("Invalid Input")
else:
    s=0
    c=0
    while(a>0):
        r=a%10
        if(c%2==0):
            s=(s)+r
        c=c+1
        a=int(a/10)
    print(s)
