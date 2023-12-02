#                         TO FIND THE NUMBER HAVING MAXIMUM NUMBER OF FACTORS
l=[]
for a in range(0,100):
    x=0
    for i in range(2,a):
        if a%i==0:
            x=x+1 
    l.append(x)
b=max(l)
c=l.index(b)
print(c)
