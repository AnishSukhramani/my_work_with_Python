import colorama
from colorama import Fore, Back, Style
from colorama.initialise import init
colorama.init(autoreset=True)

import re
a=str(input())
x=a.lower()
x_no_space=re.sub(r'\s', '',x)

def encrypt(string, length):
    return ' '.join(string[i:i+length] for i in range(0,len(string),length))

y=encrypt(x_no_space,3)

a1=y.replace("a","C")
a2=a1.replace("b","D")
a3=a2.replace("c","E")
a4=a3.replace("d","F")
a5=a4.replace("e","G")
a6=a5.replace("f","H")
a7=a6.replace("g","I")
a8=a7.replace("h","J")
a9=a8.replace("i","K")
a10=a9.replace("j","L")
a11=a10.replace("k","M")
a12=a11.replace("l","N")
a13=a12.replace("m","O")
a14=a13.replace("n","P")
a15=a14.replace("o","Q")
a16=a15.replace("p","R")
a17=a16.replace("q","S")
a18=a17.replace("r","T")
a19=a18.replace("s","U")
a20=a19.replace("t","V")
a21=a20.replace("u","W")
a22=a21.replace("v","X")
a23=a22.replace("w","Y")
a24=a23.replace("x","Z")
a25=a24.replace("y","A")
a26=a25.replace("z","B")
print(" ")
print(" ")
print(Fore.LIGHTGREEN_EX + Style.BRIGHT + Back.BLUE + a26)