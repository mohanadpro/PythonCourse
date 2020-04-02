def Fib(num):
    lstNum=[];

    for x in range(0,num):
         if (x == 0):
             lstNum.append(0)
         elif (x == 1 or x == 2):
             lstNum.append(1)
         elif(x>2):
            val=lstNum[-1]+lstNum[-2]
            if(val>num):
                break
            else:
                lstNum.append(val)
    for y in lstNum:
         print(y,end="\t")


Fib(100)