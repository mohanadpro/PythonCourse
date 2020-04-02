from functools import *

marks=[43,66,78,34,55,88,45,87]

successPeople=list(filter(lambda x:x>=60,marks))

doubleMark=list(map(lambda x:x*2,successPeople))

sum=reduce(lambda x,y:x+y,doubleMark)

print(sum,doubleMark)