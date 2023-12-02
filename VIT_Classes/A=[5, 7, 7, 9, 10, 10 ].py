A=[5, 7, 7, 9, 10, 10 ]
tempA=[]
A.sort()
for i in range(len(A)):
    if A[i]!=A[i+1]:
        tempA.append(A[i])
        A.remove(A[i])
print(tempA)