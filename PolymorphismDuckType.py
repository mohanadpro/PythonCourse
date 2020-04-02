
# In the programming if you have a bird which swimm like a duck fly like a duck walk like a duck so it's a duck no matter what it is

class Programing:

    def Code(self,IDE):
        IDE.execute()

# First IDE behave which should has an execute method
class FirstIDE:

    def execute(self):
        print("First IDE behave")

# Second IDE behave which should has an execute method
class SecondIDE:

    def execute(self):
        print("Second IDE behave")

IDE=SecondIDE()
p1=Programing()

p1.Code(IDE)