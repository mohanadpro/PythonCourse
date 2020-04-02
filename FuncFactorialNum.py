def Factorial(num):
    sum=1;
    if(num==1 or num==0):
        print(1)
    elif(num>1):
        for x in range(1,num+1):
            sum*=x;
    return  sum;

x=Factorial(4)
print(x)