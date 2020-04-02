from ModuleInPython import *

def manipulateNumber(number,number1):
    sum1=sum(number,number);
    sub1=sub(number,number1);
    mul1=mult(number,number1)
    div1=div(number,number1);
    return  sum1,sub1,mul1,div1;

sum1,sub1,mul1,div1=manipulateNumber(10,5);
print(sum1,sub1,mul1,div1);