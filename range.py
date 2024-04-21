"""Write a program to print all even numbers in range .
if starting range is greater than ending range print 'INVALID RANGe' """
a=int(input())
if(a<=0):
    print("INVALID RANGe")
else:
    for i in range(1,a+1):
        print(i)
