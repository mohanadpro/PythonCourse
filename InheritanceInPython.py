class Peron:
    def __int__(self,name,age):
        self.name=name;
        self.age=age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def showPerson(self):
        print(self.name,self.age)

class ClassRoom:

    def __init__(self,classNo,deskNo):
        self.classNo=classNo
        self.desksNo=deskNo

    def showClass(self):
        print(self.classNo,self.desksNo)

class Student(Peron,ClassRoom):

    def __init__(self,subjects,classRoom):
        self.subjects=subjects
        self.classRoom=classRoom

    def showStudent(self):
        for item in self.subjects:
            print(item)

class Teacher(Peron,ClassRoom):

    def __init__(self,subjects):
        self.subjects=subjects

    def showTeacher(self):
        print(self.name,self.age,self.classNo)
        for item in self.subjects:
            print(item)


t1=Teacher(['M','t','et'])
t1.name='maher'
t1.age=34
t1.classNo=2
t1.desksNo=35

t1.showPerson()
