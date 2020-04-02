from numpy import *

marks=matrix(array([
    [1,2,3],
    [4,5,6]
]))

marks1=matrix(array([
    [1,1],
    [2,2],
    [3,3]
]))

matrix = { (i,j):0 for i in range(5) for j in range(4) }

sum=0;

for finddimentionalTR in range(2):
    for finddimentionalTC in range(2):
        for findCounterForColumn in range(3):
            sum=sum+marks[finddimentionalTR,findCounterForColumn]*marks1[findCounterForColumn,finddimentionalTR];
            matrix[finddimentionalTR][finddimentionalTC]=sum
        sum=0

print(matrix)