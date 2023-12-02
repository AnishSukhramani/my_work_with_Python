#                     Factors of a number 

# a=int(input())
# for i in range(1,a):
#     if a%i==0:
#         print(i)



#                     Prime Factor Of a Number

# m=int(input())
# for i in range(2,m):
#     if (m%i==0):
#         print(i)
#         break
# if(m-1==i):
#     print('prime')

#                     TRYING TO REDUCE THE TIME TAKEN BY THE ABOVE CODE
import math
m=int(input())
n=int(math.sqrt(m))
for i in range(2,n+1):
    if (m%i==0):
        print(i)
        break
if(n-1==i):
    print('prime')