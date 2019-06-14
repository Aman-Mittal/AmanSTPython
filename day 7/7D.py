def PrintBlue():
    print('You chose blue!\n')
    return
def PrintRed():
    print('You Chose Red!\n')
    return

def PrintOrange():
    print("You chose Oramge!\n")
    return
def PrintYellow():
    print ("you chose yellow!\n")
    return
def choice():
    print("0:Blue")
    print("1:Red")
    print("2:Orange")
    print("3:Yellow")
    print("4:Quit")
    return
ColorSelect={ 0:PrintBlue,1:PrintRed,2:PrintOrange,3:PrintYellow}
selection=0
while True: #(selection!=4):
    if selection==4:break
    choice()
    selection=int(input("select a color option:"))
    if(selection>=0)and(selection<4):
        #print('%s'%(ColorSelect[selection]))#()
        ColorSelect[selection]()
        
