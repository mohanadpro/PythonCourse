

for val in range(1,100):
    if(val%2==0 and val%5==0 and val%10==0):
        break
    else:
        print("odd number " +str(val))