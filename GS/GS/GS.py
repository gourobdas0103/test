import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib
import requests
from pprint import pprint
from selenium import webdriver


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("Welcome back!")
    hour = int(datetime.datetime.now().hour)
    print(hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S") 
    print(Time)
    print(date)
    print(month)
    print(year)
    speak("the current Time is")
    speak(Time)
    speak("the current Date is")
    speak(date)
    speak(month)
    speak(year)
    if hour>=6 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    elif hour>=18 and hour<24:
        speak("Good Evening!")

    else:
        speak("Good Night!")

    speak("GS at your service! Please tell me how can I help you?")
#wishMe()
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query} \n")

    except Exception as e:
        print(e)
        print("Please say that again...")
        speak("Please say that again...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gourabdas0987@outlook.com', 'kalilinux@gourab0987')
    server.sendmail('gourabdas0987@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search in chrome' in query:
            speak("what should i search?")
            chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s' #Add the Location of the chrome browser

            r = sr.Recognizer()

            with sr.Microphone() as source:
                print('Say something!')
                audio = r.listen(source)
                print("done")
            try:
                text = r.recognize_google(audio)
                print('Google thinks you said: \n' +text +'.com')
                wb.get(chrome_path).open(text+'.com')
            except Exception as e:
                print(e)
        
        elif 'how is the weather' and 'weather' in query:

            url = 'https://api.openweathermap.org/'#Open api link here

            res = requests.get(url)

            data = res.json()

            weather = data['weather'] [0] ['main'] 
            temp = data['main']['temp']
            wind_speed = data['wind']['speed']

            latitude = data['coord']['lat']
            longitude = data['coord']['lon']

            description = data['weather'][0]['description']
            speak('Temperature : {} degree celcius'.format(temp))
            print('Wind Speed : {} m/s'.format(wind_speed))
            print('Latitude : {}'.format(latitude))
            print('Longitude : {}'.format(longitude))
            print('Description : {}'.format(description))
            print('weather is: {} '.format(weather))
            speak('weather is : {} '.format(weather))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)


        elif 'email to harry' and 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ReciversEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I'm sorry. I am not unable to send this email.")      

        elif 'open code' in query:
            codePath = "C:\\Users\\goura\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" #ADD THE PATH OF THE PROGEM HERE
            os.startfile(codePath)


        elif 'open' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))


        elif 'it\'s my birthday today' in query:
            print(" Wow! Wish you a very Happy Birthday")
            speak(" Wow! Wish you a very Happy Birthday")
    
        elif "where is" in query:
            data = query.split(" ")
            location = data[2]
            speak("Hold on, I will show you where " + location + " is.")
            os.system('cmd /k "start chrome https://www.google.nl/maps/place/"'+ location)
            # os.system("start chrome https://www.google.nl/maps/place/" + location  

        #open youtube
        elif 'GS open youtube' in query:
         wb.open("www.youtube.com")

        #open google
        elif 'GS open github' in query:
            wb.open("www.github.com")

        #open stackoverflow
        elif 'GS open stackoverflow' in query:
            wb.open("www.stackoverflow.com")

       #time
        elif 'GS what is the time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\goura\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)  

        elif 'go offline' in query:
            speak("Shutting down the system")
            quit()
