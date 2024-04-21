"""
Write a program to perform Addition, Subtraction,
Multiplication and Division of 2 Numbers based on the
user inputs by using Switch condition.(+ , - , * , /, %).
"""
a=int(input())
b=int(input())
c=input()
match c:
    case "+" :
        print(a+b)
    case "-":
        print(a-b)
    case "%":
        print(a%b)
    case "/":
        print(a/b)
    case "*":
        print(a*b)
        
