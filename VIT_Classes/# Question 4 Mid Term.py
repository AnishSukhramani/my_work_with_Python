# Question 4 Mid Term 
n=int(input('Enter n'))
s=n-1
for i in range(0,n):
    for j in range(0,s):
        print(end=' ')
    s=s-1
    for k in range(0,i+1):
        print('*', end=' ')
    print()