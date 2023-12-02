n=int(input())
a='0 1 '
for i in range (2,n+1):
    x=(i-1)
    y=(i-2)
    m=str(x+y)
    a=a+m+' '
print(a)