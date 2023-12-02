#   Question 2 Mid Term
n=int(input('Enter n'))
mylist=[int(item) for item in input('Enter list').split()]
s=sum(mylist)
total=(n*(n+1))/2
print(int(total-s))