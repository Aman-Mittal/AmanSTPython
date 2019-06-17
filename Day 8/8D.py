
try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
except ValueError as ob:
    print(ob)
else:
    try:
        res=num1/num2
    except ZeroDivisionError as ob:
        print(ob)
        print("divide by zero is not allowed")
    else:
        print(num1,"/",num2,"=",res)

print("Thanks")
