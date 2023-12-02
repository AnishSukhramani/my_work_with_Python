n=int(input())
s=0
t=1
for i in range(1,2*n,2):
    s=s+i*t
    t=(-1)*t
print(s)