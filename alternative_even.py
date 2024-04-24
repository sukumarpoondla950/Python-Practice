"""Write a program to print all alternative even numbers in the given
range if no numbers then print NO NUMBERS if starting range is greater
than ending range print INVALID INPUTS"""
a=int(input())
b=int(input())
c=0
if(a>b):
    print("INVALID INPUTS")
else:
    for i in range(a,b+1):
        if(i%2==0):
            if(c%2==0):
                print(i,end=" ")
            c=c+1
    if(c==0):
        print("no numbers")
        
        
