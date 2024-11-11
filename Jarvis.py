import datetime
import os
import smtplib #for email
import webbrowser #to open websites
import calendar
import pyttsx3 #for voice
from PIL import Image
import speech_recognition as sr
import wikipedia
from GoogleNews import GoogleNews
from googletrans import Translator
import yagmail
#import google
import play_requests
import pywhatkit
import PyQt5
import bs4
import requests
import sys
from bs4 import BeautifulSoup
import pyjokes
import times
from tkinter import*
from PIL import ImageTk
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good morning Sir ")
        speak("Good morning Sir ")

    elif hour>=12 and hour<18:
        print("Good Afternoon Sir ")
        speak("Good Afternoon Sir ")

    else:
        print("Good Evening Sir ")
        speak("Good Evening Sir ")

    speak("I am jarvis ")
    speak("How can I help you?")


def takecommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said: {}\n".format(query))

    except Exception as e:
        print(e)
        return "none"
    return query.lower()


def sendEmail(to, content):
    try:
        # initializing the server connection
        yag = yagmail.SMTP('pythonnotificationuser@gmail.com','nzhapmrdygbfjwpi')
        # sending the email
        yag.send(to, 'Testing Yagmail', content)
        speak("Email sent successfully")
    except:
        speak("Error, email was not sent")


def set_system_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level, None)


def increase_volume(increment = 0.05):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = min(1.0, current_volume + increment)
    set_system_volume(new_volume)
    print(f"Volume increased to {new_volume * 10:.0f}%")

def decrease_volume(decrement = 0.05):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = max(0.0, current_volume - decrement)
    set_system_volume(new_volume)
    print(f"Volume decreased to {new_volume * 100:.0f}%")


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    print("Today's date is ", day, month, year)
    speak("Today's date is ")
    speak(day)
    speak(month)
    speak(year)


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print("Current time is ", Time)
    speak("Current time is ")
    speak(Time)


def showCalendar():
    print("Please tell the year,Sir ")
    speak("Please tell the year,Sir ")
    yr = int(takecommand().lower())
    print("Please tell the month,Sir ")
    speak("Please tell the month,Sir ")
    mon = int(takecommand().lower())
    print(calendar.month(yr, mon))


def helpme():
    print("You can use the following commands:")
    speak("You can use the following commands:")
    print("1.search \n 2.show calender \n 3.Today's date \n 4.Send email \n 5.Open <site_name>")
    speak("1.search 2.show calender 3.Today's date 4.Send email 5.Open <site_name>")
    print("6.Play music \n 7.Current Time \n 8.Slideshow \n 9.News \n 10.Close \n 11.Shutdown")
    speak("6.Play music 7.Cuurent Time 8.Slideshow 9.News 10.Close 11.Shutdown")


def news():
    googlenews = GoogleNews('en','d')
    googlenews.search("India")
    googlenews.getpage(1)
    googlenews.result()
    #Separate each news (use , as separator)
    print(googlenews.gettext())
    speak(googlenews.gettext())

def trans():
    print("From which language should I translate Sir : ")
    speak("From which language should I translate Sir : ")
    sc = takecommand()
    print("Into which language should I translate Sir : ")
    speak("Into which language should I translate Sir : ")
    dt = takecommand()

    print("What should I translate Sir ?")
    speak("What should I translate Sir ?")
    sentence = takecommand()
    translator = Translator()
    #create database for language name and language code
    if "English" in sc and "Marathi" in dt:
        translated_sentence = translator.translate(sentence, src='en', dest='mr')
    elif "Marathi" in sc and "English" in dt:
        translated_sentence = translator.translate(sentence, src='mr', dest='en')
    elif "English" in sc and "Japanese" in dt:
        translated_sentence = translator.translate(sentence, src='en', dest='ja')
    elif "Japanese" in sc and "English" in dt:
        translated_sentence = translator.translate(sentence, src='ja', dest='en')
    print(translated_sentence.text)
    speak(translated_sentence.text) #error


if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query and 'jarvis' in query:
            speak('Searching Wikipedia...')
            query = query.replace("jarvis wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open' in query and 'jarvis' in query:
            if 'youtube' in query:
                speak("which video you want to play?")
                command = takecommand()

                #print(command)

                song = command.replace('play', "")
                speak('playing' + song)
                pywhatkit.playonyt(song)


            elif 'google' in query:
                speak("what should search on google?")
                #text = r.recognize_google(audio)
                url = 'https://www.google.co.in/search?q='
                search_url = url + takecommand()
                webbrowser.open(search_url)

            elif 'twitter' in query:
                 webbrowser.open("twitter.com")
            else:
                print("Sir,please specify the url")
                speak("Sir,please specify the url")
                url = takecommand().lower()
                try:
                    webbrowser.open(url)
                except Exception as e:
                    print(e)
                    print("Sorry Sir,I can't open this site right now")
                    speak("Sorry Sir,I can't open this site right now")

        elif 'play music' in query and 'jarvis' in query:
            music_dir ='D:\\Final_yr_project\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'email' in query and 'jarvis' in query:
            try:
                to = []
                print("What should I say?")
                speak("What should i say?")
                content = takecommand()
                print("Whom should I send?")
                speak("Whom should I send?")
                recipient = takecommand()
                if 'dhanashree' in recipient:
                    to.append("dambadkar494@gmail.com")
                if 'ayushi' in recipient:
                    to.append("ayushimohkar1525@gmail.com")
                else:
                    to.append('kthotange1111@gmail.com')
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif "increase volume" in query and 'jarvis' in query:
            increase_volume()
        elif "decrease volume" in query and 'jarvis' in query:
            decrease_volume()

        elif "date" in query and 'jarvis' in query:
            date()

        elif "translate" in query and 'jarvis' in query:
            trans()

        elif 'joke' in query and 'jarvis' in query:
            speak(pyjokes.get_joke())

        elif "time" in query and 'jarvis' in query:
            time()

        elif "calendar" in query and 'jarvis' in query:
            showCalendar()

        elif "help me" in query and 'jarvis' in query:
            helpme()

        elif "show notice" in query and 'jarvis' in query:
           try:
                img_dir = r'C:\Users\chede appliances\Downloads\New folder'
                imgs = os.listdir(img_dir)
                for i in imgs:
                    print(i)
                    img = r"C:\Users\chede appliances\Downloads\New folder" + i
                    im = Image.open(img)
                    im.show()
                    time.sleep(5)
                    im.close()
           except Exception as e:
                print(e)

        elif "news" in query and 'jarvis' in query:
            news()

        elif "how are you" in query and 'jarvis' in query :
            print("I am fine,Sir")
            speak("I am fine,Sir")

        elif "who are you" in query and 'jarvis' in query:
            print("I am Jarvis,Sir")
            speak("I am Jarvis,Sir")

        elif "Who made you" in query and 'jarvis' in query:
            print("I was made by  ........")
            speak("I was made by ........")

        elif "What can you do for me" in query and 'jarvis' in query:
            print("I can do many things like play music ,search wikipedia ,send email, show today's date ,time and many more")
            speak("I can do many things like play music ,search wikipedia ,send email, show today's date ,time and many more")

        elif "who i am" in query:
            speak("If you talk then definately your human.")

        elif "why you came to world" in query:
            speak("Thanks to Team codeblack. further It's a secret")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you ask me that")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "close" in query and 'jarvis' in query:
            try:
                if "age" in query:
                    os.system("taskkill /f /im iexplorer.exe")
                elif "chrome" in query:
                    os.system("taskkill /f /im chrome.exe")
                elif "youtube" in query:
                    os.system("taskkill /f /im chrome.exe")
                elif "slider" in query:
                    os.system("taskkill /f /im slider")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able")


        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takecommand())
            time.sleep(3)
            print(a)

        elif "shutdown" in query and 'jarvis' in query:
             print("Bye Sir.Have a nice day.")
             speak("Bye Sir.Have a nice day.")
             os.system('shutdown/s')
             os.sys.exit()
             quit()

