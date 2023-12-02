length=int(input('ENTER LENGTH OF SERIES'))
f2,f1=0,1
while(length):
    print(f2,end=' ')
    fn=f1+f2
    f2,f1=f1,fn
    length=length-1
