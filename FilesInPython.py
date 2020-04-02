
# open file to read the value
file=open('keyFile','r')

# write data in file 'a' for append the value appends to the previous value
# 'w' for add(every time the file clears and writes a new value)
# file=open('keyFile','a')
# for i in range(10):
#     file.write('line '+str(i) +'\n')



file1=open('copiedFile','a')

# loop on the entire file
for line in file:
    x=line+' test'
    file1.write(x)