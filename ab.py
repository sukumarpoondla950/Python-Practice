#Write a program to print A,B in given number of times alternatively
a=int(input())
for i in range(1,a+1):
    if(i==1):
        print("A,B",end="")
    else:
        print(",A,B",end="")
