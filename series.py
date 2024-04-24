"""
Write a Program to Print the following series 2*3,3*4,4*5,......16*17
(Print in two ways – Pattern & Multiplied value) 
"""
a=int(input())
b=int(input())
if(a>b):
    t=a
    a=b
    b=t
for i in range(a,b+1):
    if(i!=a):
        print(",",end="")
    print(i,"*",(i+1),end="")
    

