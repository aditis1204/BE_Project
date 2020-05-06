### Put inputquery file at the last in a newly created list
import os
import F7
from F7 import main
def func1():
    with open('filename1') as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in open('filename1')]

    print(lines)
    l = []
    for i in lines:
        if i!='inputquery.txt':
            l.append(i)
    l.append('inputquery.txt')
    a1=l[0]
    a2=l[1]
    a3=l[2]
    a4=l[3]
    a5=l[4]
    a6=l[5] 
    print(a1,a2,a3,a4,a5,a6)  
    #for i in l:
     #   s+=" "+i
    #print(s)
    F7.main(a1,a2,a3,a4,a5,a6)
   
