from datetime import *
class Student:

    school='Alamal'

    def __int__(self,name,age):
        self.name=name
        self.age=age
    # this type of method which names as 'instance method' treats with instance variables(variables in self)
    def getStudent(self):
        return self.name+' '+str(self.age)

    #this type of method treats with static variables
    @classmethod
    def setSchool(cls,school):
        cls.school=school

    #this type of method do some buisness without treating with any type of variables
    @staticmethod
    def printDate():
        print(date.today().strftime('%d/%m/%Y'))
        print((datetime.now().strftime('%H:%M:%S')))


s1=Student()

s1.printDate()