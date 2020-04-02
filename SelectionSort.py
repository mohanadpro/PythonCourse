


def SelectionSort(lst):
    temp=0
    for ite in range(len(lst)-1):
        pos = -1
        minVal = max(lst)
        for Col in range(ite,len(lst),1):
            if(minVal>lst[Col]):
                minVal=lst[Col]
                pos=Col
        if(pos!=-1):
            temp=lst[ite]
            lst[ite]=minVal
            lst[pos]=temp
    return lst

lst=SelectionSort([34,433,43,62,12,45,34,23,4,1,256,7,3,4,7])
print(lst)



lst=[43,42,5,1,2];
