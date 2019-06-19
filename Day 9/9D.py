class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color

class Cat(Animal):
    def mew(self):
        print("Cat meows")
class Dog(Animal):
    def bark(self):
        print("woof")
if __name__=="__main __":
    pet1=Dog('tomy','brown')
    pet2=Cat('Lucy','White')
    pet2.mew()
    pet1.bark()
    print(pet1.name)
    print(pet2.name)

