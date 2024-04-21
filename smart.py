"""
write a progrm to perform given tasks

Declare & initialize a number.

Check whether the number is in range 0-100 or not.

If not in range print INVALID INPUT

Else – if the number is in range 91-100 then print SUPER SMART,

81-90 print SMART,

71-80 print SMART ENOUGH,

61-70 print JUST SMART,

36-60 print NO SMART,

0-35 print DUMB.
"""
a=int(input())
if(a>100 or a<0):
    print("INVALID INPUT")
elif(a<101 and a>92):
    print("SUPER SMART")
elif(a>91 and a<82):
    print("SMART")
elif(a>70 and a<81):
    print("SMART ENOUGH")
elif(a>62 and a<71):
    print("JUST SMART")
elif(a<61 and a>35):
    print(" NO SMART")
else:
    print("DUMB")
