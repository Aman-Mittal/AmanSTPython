class Wolf:
    price = 500

    def __init__(self,name,color):
        self.name=name
        self.color=color

    def bark(self):
        print("grrrr...")
class Dog(Wolf):
    def bark1(self):
        print("Woof")

if __name__=="__main__":
    pet1=Dog("tomy","brown")
    pet1.bark()
    pet2=Wolf('Jimmy','Grey')
    pet1.bark1()
    Dog('abc','xyz').bark()

