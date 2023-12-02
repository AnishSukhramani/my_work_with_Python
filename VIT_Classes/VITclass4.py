# s1={1, 3.24 , 'vit', '1' }
# # add
# s1.add(23)
# print(s1)
# # remove
# s1.remove(1)
# print(s1)
# # pop - this does not have a value it just randomly gives an element from the set even if its a string 
# s1.pop()
# print(s1.pop())
# # discard same as removebut does not show error if you want to remove an element that is not in the set unlike remove function 
# s1.discard(9)
# print(s1)
# # dictionary
# # d1={ 'ram': 123, 'shyam ': 234 , 'ham':345 }
# # print(d1)
# # type(d1)
# # <class 'dict' >
# # key1-d1.keys()
# # print(d1)

a=int(input())
b=a%2
if(b>0):
    print('odd')
else:
    print('even')