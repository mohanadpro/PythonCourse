sum = 1
def Factorial(num):

    if(num==1):
        return 1
    else:
        return  num*Factorial(num-1)

x=Factorial(5)
print(x)