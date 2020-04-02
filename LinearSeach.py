pos=-1
def LinearSeach(list,item):
    for i in range(len(list)):
        if(list[i]==item):
            globals()['pos']=i
            return True
    return False

LinearSeach([2,4,124,5,12,34,1,5],44)

if(pos==-1):
    print("Not found")
else:
    print("Found at ",pos)