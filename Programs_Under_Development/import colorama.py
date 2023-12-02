import colorama
from colorama import Fore, Back, Style
from colorama.initialise import init
colorama.init(autoreset=True)

import re

# print(" ")
# print(" ")
# print(" ")
# print(" ")
# print(" ")
# print(" ")
# print(" ")
print( Fore.LIGHTGREEN_EX + Back.BLUE + Style.BRIGHT + "Welcome back sir! How can I help?")
a="Sir"
print( " ")
print( Fore.LIGHTGREEN_EX + Back.BLUE + Style.BRIGHT + "VERY NICE TO MEET YOU ", a )
print(" ")
print(Fore.LIGHTGREEN_EX + Back.BLUE + Style.BRIGHT + "I CAN PROVIDE YOU INFORMATIONAL AND MATHEMATICAL HELP ")
print(Fore.LIGHTGREEN_EX + Style.BRIGHT +  "Enter 1 for Informational and 2 for Mathematical Assistance")
print(Fore.RED + Style.BRIGHT +  "IN CASE OF EMERGENCY ENTER 3 ")
b=float(input())
if (0<b<2) :
    print( Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "HERE IS A LIST OF THINGS THAT I CAN DO FOR YOU")
    print(Fore.LIGHTGREEN_EX + Style.DIM + "ACCESS YOUR CONTACTS" + Fore.RED + "-------------------" + Fore.MAGENTA + "ENTER 1")
    print(Fore.LIGHTGREEN_EX + Style.DIM + "Access Email IDs" + Fore.RED + "-----------------------" + Fore.MAGENTA + "ENTER 2")
    print(Fore.LIGHTGREEN_EX + Style.DIM + "IMPORTANT BIRTHDATES" + Fore.RED + "-------------------" + Fore.MAGENTA + "ENTER 3")
    print(Fore.LIGHTGREEN_EX + Style.DIM + "ACCESS NOTES" + Fore.RED + "---------------------------" + Fore.MAGENTA + "ENTER 4")
    print(Fore.LIGHTGREEN_EX + Style.DIM + "SEMESTER-WISE LIST OF SELECTED COURSES" + Fore.RED + "-" + Fore.MAGENTA + "ENTER 5")
# ACCESS UNACTIVE MAIL IDS (PASSWORD PROTECTED)
# GPA AND CGPA OF EACH SEMESTER / YEAR 
# LIST OF BOOKS READ BY ANISH
# 
# EMERGENCY CONTACT NUMBERS eg police, ambulence, etc in various countries 
    d=float(input())
    if (0<d<2):
        print('List of Contacts is not yet updated please try again later :(')
    elif(1<d<3):
        print(" ")
        print(" ")
        print( Fore.GREEN + Style.BRIGHT + "The following data is sensetive kindly enter the password")
        x=float(input())
        if (24072002<x<24072004):
            print( Fore.LIGHTBLUE_EX + Style.BRIGHT + "Welcome ANISH here are your important Emails IDs and other information. ")
        elif (10101971<x<10101973):
            print( Fore.LIGHTBLUE_EX + Style.BRIGHT + "Welcome RAJESH here are your important Emails IDs and other information. ")
        elif (690972<x<690974):
            print( Fore.LIGHTBLUE_EX + Style.BRIGHT + "Welcome SAKHSHI here are your important Emails IDs and other information. ")
        else:
            print(Fore.RED + Style.BRIGHT + "ACCESS DENIED")
            print(Fore.RED + Style.BRIGHT + "VIEWING SOMEONE'S PERSONAL DATA WITHOUT PERMISSION IS A CRIME YOU HAVE 2 ATTEMPTS LEFT AFTER WHICH LOCAL CYBER CRIME DEPARTMENT WILL BE CONTACTED BASED UPON YOUR LOCATION.")
            
        



elif (1<b<3) :
    print( Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "HERE IS A LIST OF THINGS THAT I CAN DO FOR YOU")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "Addtion" + "                              " + Fore.MAGENTA + "ENTER 1")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "Substraction" + "                          " + Fore.MAGENTA + "ENTER 2")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "Multiplication" + "                        " + Fore.MAGENTA + "ENTER 3")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "Division" + "                              " + Fore.MAGENTA + "ENTER 4")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "6 Value Average" + "                       " + Fore.MAGENTA + "ENTER 5")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "Percentage" + "                            " + Fore.MAGENTA + "ENTER 6")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "Percentile" + "                            " + Fore.MAGENTA + "ENTER 7")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "Raise to Power" + "                        " + Fore.MAGENTA + "ENTER 8")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "Simple Intrest" + "                        " + Fore.MAGENTA + "ENTER 9")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "Compound Intrest" + "                      " + Fore.MAGENTA + "ENTER 10")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "Area of a Circle" + "                      " + Fore.MAGENTA + "ENTER 11")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "Pythagoras' Formula" + "                   " + Fore.MAGENTA + "ENTER 12")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "Einstein's Mass Energy Equivalence" + "    " + Fore.MAGENTA + "ENTER 13")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "FOUR DIGIT Binary to Decimal" + "          " + Fore.MAGENTA + "ENTER 14")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "English to Binary Coder" + "               " + Fore.MAGENTA + "ENTER 15")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "Modular Division" + "                      " + Fore.MAGENTA + "ENTER 16")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "Area of Triangle with known sides" + "     " + Fore.MAGENTA + "ENTER 17")
    print( Fore.LIGHTGREEN_EX + Style.DIM + "English to Enigma Encoder" + "             " + Fore.MAGENTA + "ENTER 18")
    
    c=float(input())
    if (0<c<2) :
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "INITIALISING SUMMATION :- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER FIRST NUMBER")
        x=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER SECOND NUMBER")
        y=float(input())
        sum=x+y
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + 'THE SUM OF THE ENTERED NUMBERS IS = ',sum)
    elif (1<c<3) :
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "INITIALISING DIFFERENCE :- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER FIRST NUMBER")
        x=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER SECOND NUMBER")
        y=float(input())
        sum=x-y
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + 'THE DIFFERENCE OF THE ENTERED NUMBERS IS = ',sum)
    elif (2<c<4) :
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "INITIALISING PRODUCT :- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER FIRST NUMBER")
        x=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER SECOND NUMBER")
        y=float(input())
        sum=x*y
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + 'THE PRODUCT OF THE ENTERED NUMBERS IS = ',sum)
    elif (3<c<5) :
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "INITIALISING DIVISION :- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER DIVIDEND/NUMERATOR")
        x=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER DIVISOR/DENOMINATOR")
        y=float(input())
        sum=x/y
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + 'THE DIVISION OF THE ENTERED NUMBERS IS = ',sum)
    elif (4<c<6) :
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "INITIALISING AVERAGE:- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER FIRST NUMBER")
        x1=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER SECOND NUMBER")
        x2=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER THIRD NUMBER")
        x3=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER FOURTH NUMBER")
        x4=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER FIFTH NUMBER")
        x5=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER SIXTH NUMBER")
        x6=float(input())
        print(" ")
        sum=(x1+x2+x3+x4+x5+x6)/6
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + 'THE AVERAGE OF THE ENTERED NUMBERS IS = ',sum)
    elif (5<c<7) :
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "INITIALISING PERCENTAGE:- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER FIRST NUMBER/OBTAINED VALUE/MARKS SCORED")
        x=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER SECOND NUMBER/MAXIMUM VALUE/OUT OF/MAXIMUM MARKS")
        y=float(input())
        sum=(x/y)*100
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + 'THE PERCENTAGE OF THE ENTERED NUMBERS IS = ',sum, "%")
    elif(6<c<8):
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "INITIALISING PERCENTILE:- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER TOTAL NUMBER OF STUDENTS APPEARED ")
        print(Fore.RED +Style.BRIGHT +"NOTE:- ENTER THE NUMBER OF STUDENTS APPEARED NOT REGISTERED.")
        x=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER THE NUMBER OF STUDENTS WHO SCORED LESSER PERCENTAGE THAN YOU ")
        y=float(input())
        p=(y/x)*100
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + 'THE CALCULATED PERCENTILE IS = ',p, "%tile")
    elif (7<c<9) :
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "INITIALISING EXPONENTIAL:- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER BASE")
        x=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER POWER")
        y=float(input())
        sum=x**y
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + 'THE ANSWER IS = ',sum)
    elif (8<c<10) :
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "INITIALISING SIMPLE INTREST :- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER PRINCIPAL AMOUNT ")
        x=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER RATE OF INTREST ")
        y=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER TENURE ")
        z=float(input())
        sum=(x*y*z)/100
        h1=sum+x
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + 'TOTAL INTREST GAINED = ',sum)
        print(Fore.LIGHTGREEN_EX + Style.DIM + 'TOTAL AMOUNT GAINED = ',h1)
    elif (9<c<11) :
        print(" ")
        print(Fore.LIGHTGREEN_EX + Back.BLUE + Style.DIM + "INITIALISING COMPOUND INTREST :- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX +'ENTER PRINCIPAL AMMOUNT')
        p=float(input())
        print(Fore.LIGHTBLUE_EX +'ENTER RATE OF INTREST ')
        r=float(input())
        print(Fore.LIGHTBLUE_EX +'ENTER TENURE ')
        t=float(input())
        A=p*(1+(1/r))**(t)
        print( Fore.LIGHTGREEN_EX + Style.DIM + 'THE COMPOUNDED AMMOUNT IS = ',  A) 
    elif (10<c<12):
        print(" ")
        print(Fore.LIGHTGREEN_EX + Back.BLUE + Style.DIM + "INITIALISING CIRCULAR AREA COMPUTATIONS :- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX +'ENTER RADIUS')
        r= float(input())
        area = 3.14*r*r
        print( Fore.LIGHTGREEN_EX + Style.DIM + 'THE CALCULATED AREA IS = ',  area) 
    elif(11<c<13) :
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "INITIALISING PYTHAGOREAN THEOREM:- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER HEIGHT LENGTH ")
        x=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER BASE LENGTH ")
        y=float(input())
        sum=((x*x)+(y*y))**(1/2)
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + 'THE LENGTH OF HYPOTENUSE IS = ',sum)
    elif(12<c<14) :
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "EINSTEIN'S MASS ENERGY EQUIVALENCE :- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER MASS")
        x=float(input())
        sum=(x)*((299792458)**2)
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + 'THE EQUIVALENT ENERGY IS = ',sum)
    elif(13<c<15) :
        print(" ")
        print(Fore.LIGHTGREEN_EX + Back.BLUE + Style.DIM + "INITIALISING FOUR DIGIT Binary :- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX +"ENTER LEFTMOST DIGIT")
        a=float(input())
        print(Fore.LIGHTBLUE_EX +"ENTER NEXT DIGIT")
        b=float(input())
        print(Fore.LIGHTBLUE_EX + "ENTERN NEXT NUMBER")
        c=float(input())
        print(Fore.LIGHTBLUE_EX + "ENTER NEXT DIGIT")
        d=float(input())
        s1=a*2**3
        s2=b*2**2
        s3=c*2**1
        s4=d*2**0
        print(Fore.LIGHTGREEN_EX + Style.DIM +"THE DECIMAL VALUE IS = ", s1+s2+s3+s4)
    elif(14<c<16) :
        print(Fore.RED +Style.BRIGHT +"PROGGRAM UNDER DEVELOPMENT PLEASE COME BACK LATER")
        def text_to_binary(text):
            total_binary = ''

            for i in range(len(text)):
                binary = ''
                string_ord = ord(text[i:i+1])

                while string_ord > 0:
                    x = string_ord % 2
                    string_ord = string_ord // 2
                    binary = str(x) + str(binary)
                    total_binary += binary + ''

            print(total_binary)
        text_to_binary('') 
    elif(15<c<17):
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "INITIALISING MODULAR DIVISION :- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER DIVIDEND/NUMERATOR")
        x=float(input())
        print(" ")
        print(Fore.LIGHTBLUE_EX + "ENTER DIVISOR/DENOMINATOR")
        y=float(input())
        sum=x%y
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + 'THE ANSWER IS = ',sum)
    elif(16<c<18):
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "INITIALISING AREA OF TRIANGLE VIA SIDES :- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX + "PLEASE ENTER FIRST SIDE ")
        a=float(input())
        print(Fore.LIGHTBLUE_EX  + "PLEASE ENTER SECOND SIDE ")
        b=float(input())
        print(Fore.LIGHTBLUE_EX  + "PLEASE ENTER THIRD SIDE ")
        c=float(input())
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**(0.5)
        print(Fore.LIGHTGREEN_EX + Style.DIM + "THE AREA OF TRIANGLE IS = ",area)

    elif(17<c<19):
        print(" ")
        print(Fore.LIGHTGREEN_EX + Style.DIM + Back.BLUE + "INITIALISING ENGLISH TO ENIGMA ENCODER :- ")
        print(" ")
        print(Fore.LIGHTBLUE_EX + "Enter the message to be encoded :- ")
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
        print(Fore.LIGHTGREEN_EX + Style.DIM + a26)
    else :
        print(Fore.RED + Style.BRIGHT + "ERROR ! ")
        print(Fore.RED + Style.BRIGHT + "PLEASE ENTER NUMBERS AS PER LIST")     
elif(2<b<4) :
    print(Fore.RED + Style.BRIGHT + "emergency mode activated ")  
    print(Fore.RED + Style.BRIGHT + "initialising comand sequence : CODE RED")  
      
else :  
     print(Fore.RED + Style.BRIGHT + "ERROR ! ")
     print(Fore.RED + Style.BRIGHT + "PLEASE ENTER NUMBERS AS PER LIST")
     


# https://learnenglishteens.britishcouncil.org/skills/listening/elementary-a2-listening