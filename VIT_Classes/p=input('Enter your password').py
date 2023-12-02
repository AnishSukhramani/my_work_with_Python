p=input('Enter your password')
l=len(p)
special=': ; < = > ? @'
if l<64:
    low=upp=dig=spe=False
    for i in p:
        if i.islower():
            low=True
        if i.isupper():
            upp=True
        if i.isdigit():
            dig=True
        if i in special:
            spe=True
    if(low and upp and dig and spe and l>12):
        print('1')
    else:
        print('0')