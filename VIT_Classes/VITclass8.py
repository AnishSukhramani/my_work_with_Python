# #GCD (or HCF) of 2 numbers
# x=int(input())
# y=int(input())
# if x>y:
#     smaller=y
# else:
#     smaller=x
# i=1
# while i<smaller+1 :
#     if((x%i==0)and(y%i==0)):
#         gc=i
#     i=i+1
# print(gc)


#EUCLIDIAN METHOD
# x=int(input())
# y=int(input())
# while y==0 :
#     x=y
#     y=x%y
# print(x)

#===================================================================================================================================


# # Defining functions
# def myfunc():
#     print('hello')

# def myadd(x,y):
#     z=x+y
#     print(z)

# myfunc()
# myadd(5,22)

def gcd(x,y):
    while y==0 :
        x=y
        y=x%y
    print(x)
a=int(input())
b=int(input())
gcd(a,b)