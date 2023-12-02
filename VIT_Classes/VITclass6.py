# iteration 
# used to perform a function multiple times 
# while and for statements    https://chat.whatsapp.com/GKAAMo2NR7q4qDTMiwlVi3

#sir's method
# temp=0
# while temp<5:
#   print("Welcome to VIT")
#   temp=temp+1

# # my method
# i=5
# while i>0:
#     print("Welcome to VIT")
#     i=i-1

# p=0
# while p<10:
#     p=p+1
#     print(p)

# i=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for x in range(11):
#     print(x)

# for x in range (1,11,2):
#     print(x)

# i=str(input())
# o=len(i)
# print('No of Digits in the Number are ',o)

num=int(input())
count=0
while num!=0 :
    num=num//10
    count=count+1   
print(count)
