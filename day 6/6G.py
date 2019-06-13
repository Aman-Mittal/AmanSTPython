def add(a,b,c):
    return a+b+c
x=[1,2,3,4,5,6]
y=[10,20,30,40,50,60]
z=[11,22,33,44,55,66]
res=list(map(lambda a,b,c: a+b+c, x,y,z))
print (res)
res=list(map(add,x,y,z))
print(res)
