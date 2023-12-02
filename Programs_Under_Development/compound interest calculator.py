import colorama 
from colorama import Fore, Back, Style 
colorama.init(autoreset=True)

print(" ")
print(Fore.LIGHTGREEN_EX + Back.BLUE + Style.BRIGHT + "hello i am C.I. compound interest caculator")
print(" ")
print(Fore.GREEN +'please enter principal amount ')
p=int(input())
print(Fore.GREEN +'please enter rate of intrest ')
r=int(input())
print(Fore.GREEN +'please enter tenure ')
t=int(input())
A=p*(1+(1/r))**(t)
print( Fore.BLACK + Back.GREEN + 'the compounded amount is ',  A) 