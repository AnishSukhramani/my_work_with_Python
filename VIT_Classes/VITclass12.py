#   MY METHOD
# n=int(input('Enter number of items'))
# a=(input('Enter cost of each'))
# b=a.replace(' ',',')
# l=[]
# l.append(b)
# l.sort(reverse=True)
# h=0
# for i in range(0,n,2):
#     g=[]
#     g.append(l[i,i+1])
#     h=h+sum(g)

#   SIR'S METHOD

N=int(input('Enter number of Items'))
print(f"Enter the cost of {N} items:")
costlist=[]
for i in range(0,N):
    cost=int(input())
    costlist.append(cost)

costlist.sort()
sum=0
for i in range(N,0,-4):
    sum=sum + costlist[i-1] + costlist[i-2]
print(sum)