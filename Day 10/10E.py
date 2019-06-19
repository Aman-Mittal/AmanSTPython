def printinfo(arg1,*vartuple):
    print("output is:",arg1)
    print("Contents of variable length tuple is :")
    for var_temp in vartuple:
        print(var_temp,end='')
        print ()
        return

if __name__=='__main__':

    printinfo(10)
    printinfo(70,60,50)
    printinfo(70,60,'tea','samosas','chips','cake',50)
    
