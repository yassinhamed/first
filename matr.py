from numpy import array
from random import randint
def etap1(ch):
    m=array([int]*len(ch))
    for i in range (len(ch)):
        m[i]=ch[i]
    return(m)
def etap2(m,ch):
    pas=1
    x=0
    while x<len(ch)-1:
        nb=0
        nb1=0
        for i in range (x):
            n=int(m[i])
            nb=nb*(10**i)+n
        if nb1+1==nb:
            nb1+=1
            x+=1
        else:
            pas+=1
            x+=1
        print(pas)
ch='101112'
m=etap1(ch)
print('le tzbleau est',m)
etap2(m,ch)