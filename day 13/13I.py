import random

def str_float(x):
    for i in range(0,len(x)-1):
        x[i] = float(x[i])
    return x

data1 = []
data2 = []
for line in open("iris.txt"):
    temp = line[:-1].split(",") if line[-1]=="\n" else line.split(",")
    if random.random() <= 0.8:
        data1.append(str_float(temp))
    else:
        data2.append(str_float(temp))

print(len(data1))
print(len(data2))
print(data1)
print(data2)
