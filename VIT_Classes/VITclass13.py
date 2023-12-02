#   CONVERSION BETWEEN ONE NUMBER SYSTEM TO ANOTHER
# a=bin(9)
# print(a)

# b=oct(25)
# print(b)

# c=hex(25)
# print(c)

#   DECIMAL TO BINARY

# a=int(input())
# result=""
# while a!=0:
#     rem=a%2
#     a=a//2
#     result=str(rem)+result
# print(result)

#   DECIMAL TO BINARY USING RECURSION 

# def convert(n):
#     if n>0:
#         convert(n//2)
#         print(n%2,end='')
# convert(6)

a=int(input())
result=""
while a!=0:
    rem=a%16
    a=a//16
    result=str(rem)+result
ans=result
# if '10' in ans:
#     ans.replace('10','a')
# if '11' in ans:
#     ans.replace('11','b')
# if '12' in ans:
#     ans.replace('12','c')
# if '13' in ans:
#     ans.replace('13','d')
# if '14' in ans:
#     ans.replace('14','e')
if '15' in ans:
    ans.replace('15','f')

print(ans)