N,x,y=2,10,2
cops=[21,75]
z=x*y
for i in range(1,101):
    safe=True
    for j in range(N):
        if (cops[j]-z<=i<=cops[j]+z):
            safe=False
    if safe==False:
        print(f'C{i}', end=' ')
        