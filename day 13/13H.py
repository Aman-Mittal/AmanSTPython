import random
data1 = []
data2 = []
for line in open('iris.txt', 'r'):
    temp = line[0:-1].split(',')
    #print(temp)
    if random.random() <= 0.8:
        data1.append(temp)
    else:
        data2.append(temp)
    

print("Data1: ", len(data1))
print("Data2: ", len(data2))
#print(data)
