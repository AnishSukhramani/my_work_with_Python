p=int(input())
r=int(input())
t=int(input())
a=int(input('mothly deposit'))
while(t>0):
    s=p*((1+(1/r))**t)
    p=s+a
    t=t-1
print(s)