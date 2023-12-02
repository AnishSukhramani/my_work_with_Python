# a=[10,5,8,10,10,9,7,10,10,10,10,10,10,10,10,10,10,10,10,10]
# count=[0]*11
# for v in a:
#     count[v]=count[v]+1
# for t in count:
#     print(t,end=' ')

#METHOD 2 

a=[5, 3, 10, 2, 15]
max=a[0]
for i in range(5):
    if a[i]>max:
        max=a[i]
print(max)