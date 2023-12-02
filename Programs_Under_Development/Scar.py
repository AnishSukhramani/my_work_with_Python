#there are some modules that are yet to be installed in the command prompt window or the VS Code IDE
# Terminal commands are as follows
#pip install pyttsx3
#pip install SpeechRecognition
#pip install wikipedia
#pip install colorama
#pip install pipwin ||||| and then ||||| pipwin install pyaudio

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import re
# import pyjokes
import colorama
from colorama import Fore, Back, Style
from colorama.initialise import init
colorama.init(autoreset=True)




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT  + audio)
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir !")
def takeComand():
    r=sr.Recognizer()
    print(Fore.MAGENTA + Style.DIM + "Listening...")
    r.pause_threshold = 0.8
    audio = r.listen(source)
    audio = str(input())
    try:
        print(Fore.MAGENTA + Style.DIM+ "Rcognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(Fore.MAGENTA + Style.BRIGHT + "Anish said:", query)
    except Exception as e:
        # print(e)
        print("Say that again")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anish.scarnet@gmail.com', 'theknockofdusk') # password arises a matter of security concern hencefoth its better to always link a secure text file in case of reading password 
    server.sendmail('anish.scarnet@gmail.com', to, content)
    server.close()

if __name__=="__main__":
    wishMe()
    speak("Scar at your service, as always.")
    scar=1
    while True:
        query = takeComand().lower()
        if scar==1:
            if 'search for' in query:
                speak('Searching Wikipedia...')
                query =  query.replace("search for", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(results)
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            elif 'play music' in query:
                music_dir = 'C:\\Users\\RAJESH SUKHRAMANI\\Desktop\\PYTHON\\Scarknowledgebase'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}\n")
            elif 'open code' in query:
                codePath="C:\\Users\\RAJESH SUKHRAMANI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            elif 'email to dad' in query:
                try:
                    speak ("What should I say?")
                    content=takeComand()
                    to="sukh_rajesh@yahoo.com"
                    sendEmail(to, content)
                    speak("The Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir I am unable to send email")
            elif 'email to roommate' in query:
                try:
                    speak ("What should I say?")
                    content=takeComand()
                    to="sshasshwatyadav@gmail.com"
                    sendEmail(to, content)
                    speak("The Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir I am unable to send email")
            elif 'email to mum' in query:
                try:
                    speak ("What should I say?")
                    content=takeComand()
                    to="sakhshirajesh@gmail.com"
                    sendEmail(to, content)
                    speak("The Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir I am unable to send email")
            elif 'email to me' in query:
                try:
                    speak ("What should I say?")
                    content=takeComand()
                    to="anishsukhramani@gmail.com"
                    sendEmail(to, content)
                    speak("The Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir I am unable to send email")
            elif 'email to arya' in query:
                try:
                    speak ("What should I say?")
                    content=takeComand()
                    to="aarya2805@gmail.com"
                    sendEmail(to, content)
                    speak("The Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir I am unable to send email")
            elif 'email to aarya' in query:
                try:
                    speak ("What should I say?")
                    content=takeComand()
                    to="aarya2805@gmail.com"
                    sendEmail(to, content)
                    speak("The Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir I am unable to send email")
            elif 'email to amol' in query:
                try:
                    speak ("What should I say?")
                    content=takeComand()
                    to="amoltiwary7803@gmail.com"
                    sendEmail(to, content)
                    speak("The Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir I am unable to send email")
            elif 'email to sister' in query:
                try:
                    speak ("What should I say?")
                    content=takeComand()
                    to="pujaramvani@gmail.com"
                    sendEmail(to, content)
                    speak("The Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir I am unable to send email")
    # Mathematics
                
            elif "add two numbers" in query:
                speak('Right away sir')
                speak('What is the first number?')
                a=takeComand()
                speak('What is the second number?')
                b=takeComand()
                c=int(a)
                d=int(b)
                e=c+d
                speak('The sum is')
                speak(str(e))
            elif "add some numbers" in query:
                speak('how many numbers do you want to add?')
                a=takeComand()
                b=int(a)
                speak('what is the first number?')
                c=takeComand()
                d=int(c)
                for i in range(b-1):
                    speak('Next?')
                    e=takeComand()
                    f=int(e)
                    d=d+f
                    print('sum till now is = ', d)
                speak('The sum of the given numbers is ')
                speak(str(d))
            elif "multiply some numbers" in query:
                speak('how many numbers do you want to multiply?')
                a=takeComand()
                b=int(a)
                speak('what is the first number?')
                c=takeComand()
                d=int(c)
                for i in range(b-1):
                    speak('Next?')
                    e=takeComand()
                    f=int(e)
                    d=d*f
                    print('product till now is = ', d)
                speak('The product of the given numbers is')
                speak(str(d))
            elif "divide two numbers"  in query:
                speak("Alright sir here we go! What should I put in the numerator?")
                a=takeComand()
                speak("Noted. What should I put in the denominator?")
                b=takeComand()
                c=int(a)
                d=int(b)
                e=c/d
                speak('The answer is ')
                speak(e)
            elif "substract two numbers" in query:
                speak("Alright sir, What is the first number?")
                a=takeComand()
                speak("Okay, What is the second number?")
                b=takeComand()
                c=int(a)
                d=int(b)
                e=c-d
                speak('The difference is ')
                speak(str(e)) 

    #Chat / Response / jokes
            # elif "joke" in query:
            #     speak(pyjokes.get_jokes())
            elif "thank you" in query:
                speak('Anytime Sir')
            elif "hello" in query:
                speak('Hello sir')
            elif "it's play time" in query:
                speak('Always ready for you sir')
            elif "it's playtime" in query:
                speak('Always ready for you sir')
            elif "do you know adolf hitler" in query:
                speak('I would not consider him as a role model sir.')
            elif 'who created you' in query:
                speak('I was initially just a smart Artificially Intelligent sowtware made from scratch by Sir Anish Sukhramani')
            
            elif 'emergency' in query:
                speak('Emergency mode activated')
                #THIS PART OF CODE IS YET UNDER DEVELOPMENT 




























            elif "play a game" in query:
                speak("Actually sir, I was getting bored too, I reccommend playing 21 dares, do you want me to remind you the rules?!")
                a=takeComand().lower()
                if 'yes' in a :
                    speak('All you have to do is to say upto three numbers starting from the number where I have left! ')
                    speak('Or in case you start first, start from one!')
                    speak('As mentioned earlier you can say maximum three numbers in one turn, the one who says the number twenty one, LOOSES!!!!!!!!!!!!!')
                    speak('Are you ready sir ?')
                else :
                    speak('Are you ready sir?')
                b=takeComand().lower()
                if 'yes' in b :
                    speak("Alright, here we go!")
                    speak('one two three')
                    print('1, 2, 3')
                    c=takeComand().lower()
                    if '4' in c:
                        speak('five six seven')
                        print('5, 6, 7')
                        d=takeComand().lower()
                        if '8' in d:
                            speak('nine ten eleven')
                            print('9, 10, 11')
                            e=takeComand().lower()
                            if '12' in e:
                                speak('thirteen fourteen fifteen')
                                print('13, 14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '13' in e:
                                speak('fourteen fifteen')
                                print('14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '14' in e:
                                speak('fifteen')
                                print('15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                        elif '9' in d:
                            speak('ten eleven')
                            print('10, 11')
                            e=takeComand().lower()
                            if '12' in e:
                                speak('thirteen fourteen fifteen')
                                print('13, 14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '13' in e:
                                speak('fourteen fifteen')
                                print('14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '14' in e:
                                speak('fifteen')
                                print('15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                        elif '10' in d:
                            speak('eleven')
                            print('11')
                            e=takeComand().lower()
                            if '12' in e:
                                speak('thirteen fourteen fifteen')
                                print('13, 14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '13' in e:
                                speak('fourteen fifteen')
                                print('14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '14' in e:
                                speak('fifteen')
                                print('15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                    elif'5' in c:
                        speak('six seven')
                        print('6,7')
                        d=takeComand().lower()
                        if '8' in d:
                            speak('nine ten eleven')
                            print('9, 10, 11')
                            e=takeComand().lower()
                            if '12' in e:
                                speak('thirteen fourteen fifteen')
                                print('13, 14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '13' in e:
                                speak('fourteen fifteen')
                                print('14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '14' in e:
                                speak('fifteen')
                                print('15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                        elif '9' in d:
                            speak('ten eleven')
                            print('10, 11')
                            e=takeComand().lower()
                            if '12' in e:
                                speak('thirteen fourteen fifteen')
                                print('13, 14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '13' in e:
                                speak('fourteen fifteen')
                                print('14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '14' in e:
                                speak('fifteen')
                                print('15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                        elif '10' in d:
                            speak('eleven')
                            print('11')
                            e=takeComand().lower()
                            if '12' in e:
                                speak('thirteen fourteen fifteen')
                                print('13, 14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '13' in e:
                                speak('fourteen fifteen')
                                print('14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '14' in e:
                                speak('fifteen')
                                print('15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                    elif '6' in c:
                        speak('seven')
                        print('7')
                        d=takeComand().lower()
                        if '8' in d:
                            speak('nine ten eleven')
                            print('9, 10, 11')
                            e=takeComand().lower()
                            if '12' in e:
                                speak('thirteen fourteen fifteen')
                                print('13, 14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '13' in e:
                                speak('fourteen fifteen')
                                print('14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '14' in e:
                                speak('fifteen')
                                print('15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                        elif '9' in d:
                            speak('ten eleven')
                            print('10, 11')
                            e=takeComand().lower()
                            if '12' in e:
                                speak('thirteen fourteen fifteen')
                                print('13, 14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '13' in e:
                                speak('fourteen fifteen')
                                print('14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '14' in e:
                                speak('fifteen')
                                print('15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                        elif '10' in d:
                            speak('eleven')
                            print('11')
                            e=takeComand().lower()
                            if '12' in e:
                                speak('thirteen fourteen fifteen')
                                print('13, 14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '13' in e:
                                speak('fourteen fifteen')
                                print('14, 15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                            elif '14' in e:
                                speak('fifteen')
                                print('15')
                                f=takeComand().lower()
                                if '16' in f:
                                    speak('seventeen')
                                    print('17')
                                    g=takeComand().lower()
                                    if '18' in g:
                                        speak('nineteen twenty')
                                        print('19, 20   :)')
                                        speak('You loose sir!')
                                    elif '19' in g:
                                        speak('twenty')
                                        print('20   :)')
                                        speak('You loose , sir')
                                    elif '20' in g:
                                        speak('Ahhh!, .......... alright 21 ')
                                        speak('Not my pleasure sir but definately my duty to announce that you win')
                                        print(':(')
                                elif '17' in f:
                                    speak('eighteen nineteen twenty')
                                    print('18, 19, 20')
                                elif '18' in f:
                                    speak('NINETEEN TWENTY')
                                    print('19, 20')
                elif 'no' in b:
                    speak('Ahhhhhhhhhhh!............., what a waste of time.')
                    print(":(")