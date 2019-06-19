'''
This is the sample documentation which will help us to use documentation module
'''

class Employee:
    '''
This is the class emlpoyee
'''

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('Total Employee %d' %Employee.empCount)

    def displayEmployee(self):
        print('Name: ', self.name, ', Salary: ', self.salary)

emp1 = Employee('Nikhil', 9999)
emp1.displayEmployee()
print("is salaryan attribute: ",hasattr(emp1,'salary'))
print(getattr(emp1,'salary'))
setattr(emp1,'salary',7000)
print('Modified Salary',getattr(emp1,'salary'))
setattr(emp1,'desg','manager')
print(hasattr(emp1,'desg'))
print("Added attribute",getattr(emp1,'desg'))
delattr(emp1,'salary')
print("is salary an attribute:",hasattr(emp1,'salary'))
