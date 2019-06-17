num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
try:
    #res1=num1+num2
    res=int(num1)/int(num2)
    print(res)
except(ZeroDivisionError,ValueError,TypeError):
    print("miultiple exception panel")
except Exception as ob:
    print(ob)
else:
    print(num1,"/",num2,"=",res)
finally:
    print("thanks")
print("Visit again at VIPS")
