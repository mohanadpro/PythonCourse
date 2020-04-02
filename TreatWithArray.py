from array import *
vals=array('i',[1,23,55,21,42,32]);

Tempvals=array(vals.typecode,(a*4 for a in vals))

for x in Tempvals:
    print(x);


help('array')