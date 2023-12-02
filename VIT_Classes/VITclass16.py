#   SQUARE OF A NUMBER METHOD 1
# import math
# a=math.sqrt(16)
# print(a)

#   METHOD 2

# a=(16)**0.5
# print(a)

#   A DIFFERENT APPROACH TOWARDS SQUARE ROOT 

def mysqrt(m):
    g1=m/2
    g2=(g1+(m/g1))/2
    while (g1-g2)>0.0001 or (g2-g1)>0.0001:
        g1=g2
        g2=(g1+(m/g1))/2
    print(g2)
mysqrt(30)