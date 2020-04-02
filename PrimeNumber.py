Number=int(input("Please input number to check if it is prime or not?"))

for x in range(2,Number,1):
    if(Number%x==0):
        print("The number "+str(Number)+" is not prime")
        break
else:
    print("Your number "+str(Number)+" is a prime number")