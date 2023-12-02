# lists 
# denoted by square brackets
l= [1, 5, 7, 10 , 20 , 9 , 4, 500, 500, 500]
print(l)

#print specific elements
print(l[0])

#slice the list
x=l[1:4]
print(x)

#adds elements at the end of the list
l.append(10000023)
print(l)

# extend function - add a list to another list (the new list will be added at the end of the previous one in the order in which it is written in the list)
a=[99, 98, 97, 96, 95, 94]
l.extend(a)
print(l)

#insert function - adds elements at the index of your choice
l.insert(2, 69)
print(l)

#sort - arranges the elements in increasing value 
l.sort()
print(l)

#pop - removes the selected element from the list 
#note - do not enter the element to be removed enter its index
l.pop(2)
print(l)

#count - counts the number of times an element is repeating in the list
b=l.count(500)
print(b)

#lenght
c=len(l)
print(c)

#sum
d=sum(l)
print(d)

# * in a list means it will repeat the no. of elements the no. of times
e=[1, 2, 3]
f=e*3
print(f)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# LOOPS IN LISTS !!!!!!!!!!!!!!!
#l is the same as above 
for i in range(len(l)):
    print(l[i])
print(" ")
# input list
g=[]
n=5
for i in range(n):
    h=int(input())
    g.append(h)
print(g)
