
def BubbleSort(lst):
    temp=0
    for numOfIteration in range(len(lst)-1):
        for indCol in range(len(lst)-numOfIteration-1):
            if(lst[indCol]>lst[indCol+1]):
                temp=lst[indCol]
                lst[indCol]=lst[indCol+1]
                lst[indCol+1]=temp
    return lst


lst=BubbleSort([43,5,12,5,7,34,626,23,51,2,4])

print(lst)

