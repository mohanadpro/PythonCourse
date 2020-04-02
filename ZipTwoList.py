
names=['name1','name2','name3','name4']

marks=[25,56,32,66]

nameMarks=list(zip(names,marks))

for name,mark in nameMarks:
    print(name,mark)