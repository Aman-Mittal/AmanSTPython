def convert_str_to_float(x,n):
    for i in range(n):
        x[i]=float(x[i])
    return x

def load_split_data(split,training_data=[],test_data=[]):
    for line in open("iris.txt",'r'):
        temp=line[0:-1].split(',')
        if random.random()<=split:
            training_data.append(convert_str_to_float(temp,4))
        else:
            test_data.append(convert_str_to_float(temp,4))
        return(training_data,test_data)
                
