"""Write a Program to Print the Biggest Number out of the Given three Numbers?"""
a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
    print("the Biggest Number out of the Given three Numbers=",a)
elif(a<c and b<c):
    print("the Biggest Number out of the Given three Numbers=",c)
else:
    print("the Biggest Number out of the Given three Numbers")
    
