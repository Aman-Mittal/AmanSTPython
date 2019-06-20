import sys
sys.setrecursionlimit(5000)

def factorial(a):
    if a==0:
        return 1
    else:
        return a*factorial(a-1)
x=int(input("Enter number  :")) 

print(factorial(x))
