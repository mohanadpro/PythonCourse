def divTwoNums(FNum,SNum):
    print(FNum/SNum)


def middleFunc(func):

    def doOperationBeforCallingdivTwoNum(FNum,SNum):
        if(FNum<SNum):
            FNum,SNum=SNum,FNum;
            return func(FNum,SNum)
    return doOperationBeforCallingdivTwoNum

divTwoNums = middleFunc(divTwoNums)

divTwoNums(4,2)