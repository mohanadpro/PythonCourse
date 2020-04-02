
class Employee:
    staticVar=0;
    def __int__(self):
        pass
    def __init__(self,CPU,RAM):
        self.mycpu=CPU
        self.myram=RAM


    def getSalary(self):
        print(self.mycpu+' '+self.myram)


emp=Employee('core i7','16G')

Employee.staticVar=34

emp1=Employee('','')
print(emp1.staticVar)
emp.getSalary()