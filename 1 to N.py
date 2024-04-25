#To find 1 to N prime numbers in python
a=int(input())
if(a<=1):
    print("Not a Prime Number")
else:
    for i in range(2,a+1):
        b=True
        for j in range(2,i):
            if(i%j==0):
                b=False
                break
        if(b):
            print(i)
            
