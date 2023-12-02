# TO REMOVE THE DUPLICATE ELEMENTS FROM AN ARRAY/LIST AND 
#PRINT THE UNIQUE ONES

# A=[5, 7, 7, 9, 10, 10 ]
# tempA=[]
# A.sort()
# x=len(A)    #JUST IN CASE IF DUPLICATE NUMBERS ARE NOT ADJECENT
# for i in range(1,x):
#     m=A[i-1]
#     n=A[i]
#     if m!=n:
#         tempA.append(A[i-1])
# tempA.append(A[i])
# for j in tempA:
#     print(j,end=' ')


#       A SHORTER WAY
A=[5, 7, 7, 9, 10, 10 ]
tempA=[]
for i in A:
    if i not in tempA:
        tempA.append(i)
for j in tempA:
    print(j,end=' ')
    