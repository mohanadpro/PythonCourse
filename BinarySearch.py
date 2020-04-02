pos=-1
CountOfIteration=0
def BinarySearch(list,item):
    low=0
    heigh=len(list)-1
    mid=(low+heigh)//2
    while(low<heigh):
        globals()['CountOfIteration']=globals()['CountOfIteration']+1;
        if(list[mid]==item):
            globals()['pos']=mid
            return  True
        elif(item>=list[mid]):
            low=mid
            mid=(heigh+low)//2
        else:
            heigh=mid
            mid=(low+heigh)//2
    return False


BinarySearch([1,5,6,8,22,66,787,3344],22)

if(pos==-1):
    print("Noe found","Count of iteration "+str(CountOfIteration))
else:
    print("Found at ",pos,"Count of iteration "+str(CountOfIteration))
