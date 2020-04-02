
def OddAndEvenNum(lstNums):
    CounterForEvenNumber=0;
    CounterForOddNumber=0;
    for item in lstNums:
        if(item%2==0):
            CounterForEvenNumber+=1;
        else:
            CounterForOddNumber+=1;
    return CounterForOddNumber,CounterForEvenNumber;


oddNum,EvenNum= OddAndEvenNum([32,1541,32125,511])

print(str(oddNum) +' '+ str(EvenNum))