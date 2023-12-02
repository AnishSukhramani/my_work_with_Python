speak('how many numbers do you want to add?')
a=input()
b=int(a)
speak('what is the first number?')
c=input()
d=int(c)
for i in range(b-1):
    speak('Next?')
    e=input()
    f=int(e)
    d=d+f
    print('sum till now is = ', d)
speak(d)