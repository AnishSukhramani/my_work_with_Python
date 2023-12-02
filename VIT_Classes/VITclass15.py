# a=int(input())
# i=2
# while i!=a:
#     rem=a%i
#     i=i+1
#     if rem==0:
#         print('Not Prime')
#         break
#     else:
#         print('prime')
#         break

#   Sir's Method 
# num=int(input())
# t=0
# for i in range(2,num):
#     rem=num%i
#     if rem==0:
#         print('not prime')
#         t=1
#         break
# if t==0:
#     print('prime ')





# for i in range(1,11):
#     if i!=6:
#         print(i)

# Sir's Method - Introduction to the concept of 'CONTINUE' 
# for i in range(1,11):
#     if i==6:
#         continue
#     print(i)

# Introduction to 'PASS'

# for i in range(1,11):
#     if i%2==0:
#         pass
#     else:
#         print(i)

a=str(input())
l=['a', 'b', 'c', 'd', 'e' 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c']
i=0
while i in range(len(a)):
    b=a[i]
    c=l[b]
    x=l[c]
    a.replace(b,x)
print(a)