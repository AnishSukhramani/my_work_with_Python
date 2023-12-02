# def greater(x, y):
#     if (x-y)>0:
#         print(x)
#     elif (x-y)<0:
#         print(y)
#     else :
#         print("numbers are equal")

# x=int(input())
# y=int(input())
# greater(x,y)

# an easy method

# def maximum(a,b,c):
#     if a>b:
#         if a>c:
#             print(a)
#         else:
#             print(c)
#     else:
#         if b>c:
#             print(b)
#         else:
#             print(c)
    
# a=int(input())
# b=int(input())
# c=int(input())
# maximum(a,b,c)


# def sum(l):
#     a=len(l)
#     c=0
#     for i in range (a):
#         b=l[i:i+1]
#         c=c+b
#         i=i+1

# l=[10, 2, 4, 45 ,66, 34, 54]
# sum(l)

# def sum(l):
#     a=0
#     for i in l:
#         a=a+i
#     print(a)

# l=[1, 2, 3, 4 ]
# sum(l)

# def rev(a):
#     for i in range (len(a)):
#         r=a[::-1]
#     print(r)
# a=str(input())
# rev(a)


def fac(x):
    a=1
    for i in range(x):
        i=i+1
        a=a*i
    print(a)

x=int(input())
fac(x)