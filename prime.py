#Write a program to check given number is prime number or not.
a=int(input())
if(a<=1):
    print("Invalid Input")
else:
    b=True
    for i in range(2,a):
        if(a%i==0):
            b=False
            break
    if(b):
        print("Prime")
    else:
        print("Not a Prime")
