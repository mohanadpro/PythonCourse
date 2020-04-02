num=int(input("number of iteration"))
start=1

while(start<=num):
    print("Hello world",start)
    secondLoop = 1
    while(secondLoop<start):
        print(secondLoop)
        secondLoop=secondLoop+1
    start+=1