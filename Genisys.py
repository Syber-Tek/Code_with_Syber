import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser
import os
import requests
import pywhatkit
import pyautogui
import psutil
import pyjokes
from googlesearch import search
from googletrans import Translator
from translate import Translator 
import pyfiglet
import geocoder

# Voices
# 0 - male
# 4 - female
# 33 - female
# 32 - male
# 28 - female
# 17 - female
# 11 - female
# 7 - male
# 40 - female

# Initialize speech engineS
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[33].id)
voicespeed = 160
engine.setProperty('rate', voicespeed)
engine.runAndWait()
# Set the font to be used
font = pyfiglet.Figlet(font="larry3d")

# display name of AI
AI_name = "G e n i s y s"

# Set name of AI
bot_name = "Genisys"

search("Google", lang="en")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is")
    speak(Time)

def date():
    now = datetime.datetime.now()
    date_string = now.strftime("%B %d, %Y")
    speak("Today's date is " + date_string)

#API key for the weather
API_key = "17c6072dd30722149471605547128ece"
# Define function to get weather data
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] != "404":
            weather1 = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind = data["wind"]["speed"]
            return f"The current weather in {city} is {weather1} with a temperature of {temperature}°C, humidity of {humidity}%, pressure of {pressure} hPa, and wind of {wind} m/s."
        else:
            return "Sorry, I could not get the weather for that location"
    except requests.exceptions.RequestException as e:
        return "Sorry, there was an error getting the weather data."
    
# set the font style
n = font_style = pyfiglet.figlet_format(AI_name, font="slant")

# print the formatted text
print(n)

def wishme():
    speak("welcome sir!")

    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning Sir!")
    elif 12 <= hour < 18:
        speak("Good afternoon Sir!")
    elif 18 <= hour < 24:
        speak("Good evening Sir!")
    else:
        speak("Good night sir!")
    
    speak(bot_name + " at your service. How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please")

        return "None"
    return query

def sendEmail(to, content):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465

    # set up the SMTP server
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login('dellpc788@gmail.com', 'Namkk@15.')
    server.sendmail('narteykofi.ackam@gmail.com', to, content)
    server.quit()
    
def screenshot():
    img = pyautogui.screenshot()
    img.save('Untitled/Users/olagstem/Desktop/AI/screenshot.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = str(psutil.sensors_battery())
    speak("Battery is at")
    speak(battery.percentage)
    
def jokes():
    speak(pyjokes.get_joke())  

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
            
        elif 'date' in query:
            date()
            
        elif 'wikipedia' in query:
            speak("searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
            
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'narteykofi.ackam@gmail.com'  # Replace with the recipient's email address
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Unable to send the email.")
                
        elif 'search in chrome' in query:
            speak("What should I search?")
            search = takeCommand().lower()
            url = f'https://www.google.com/search?q={search}'
            webbrowser.open_new_tab(url)
        # elif 'play' in query:
        #     song = input_text.replace('play', '').strip()
        #     pywhatkit.playonyt(song)
        #     speak_and_print(bot_name + ":", "Playing " + song + " on YouTube")
        #     return True
        
        elif 'thanks' in query.lower():
            rest = "You're welcome! If you have any other questions or need further assistance, don't hesitate to ask."
            speak(rest)
            
        elif 'how are you?' in query.lower():
            res5 = f"I am doing great, thank you for asking. How about you?"
            speak(res5)
            about = takeCommand()
            speak('We thank God')
            
        elif "calculate" in query.lower():
            speak("Sure! Please enter the math problem.")
            problem = takeCommand()
            try:
                result = eval(problem)
                speak(f"The result of {problem} is {result}")
            except:
                speak("Sorry, I couldn't calculate the result.")
                
        elif "location" in query.lower():
            speak("Sure! Please enter the name of the location.")
            location = takeCommand()
            g = geocoder.arcgis(location)
            if g.json:
                lat, lng = g.latlng
                speak(f"The coordinates of {location} are latitude: {lat} and longitude: {lng}")
            else:
                speak(f"Sorry, I couldn't find the coordinates for {location}.")
      
    
        elif "translate" in query.lower():
            # Prompt the user for the sentence to translate
            speak("Sure! Please enter the sentence you want to translate.")
            sentence = takeCommand()

            # Prompt the user for the target language
            speak("Great! Now, please enter the language you want to translate to.")
            target_language = takeCommand()

            # Translate the sentence
            translator = Translator(to_lang=target_language)
            translation = translator.translate(sentence)

            # Output the translated sentence
            speak(f"The translated sentence is: {translation}")
            print(translation)

        elif 'logout' in query:
            speak("Logging out...")
            os.system("shutdown -1")
            
        elif 'shutdown' in query:
            speak("shutting down...")
            os.system("shutdown /s /t 1")
            
        elif 'restart' in query:
            speak("restarting...")
            os.system("shutdown /r /t 1")
            
        elif 'play music' in query:
            speak("What music will you like to play?")
            music = takeCommand().lower()
            speak("Playing"+ music + "on youtube")
            pywhatkit.playonyt(music)
            
        elif 'play song' in query:
            speak("What song will you like to play?")
            song = takeCommand().lower()
            speak("Playing"+ song + "on youtube")
            pywhatkit.playonyt(song)
            
        elif 'remember this' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said I should remember" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
            
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You said I should remember" + remember.read())
            
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
            
        elif 'cpu' in query:
            cpu()    
            
        elif 'joke' in query:
            jokes()      
                
        elif 'open website' in query.lower():
            speak('What website do you want to open?')
            website = takeCommand()
            webbrowser.open_new_tab('http://' + website) 
            
        elif 'open spotify' in query.lower():
            speak('Okay. What song would you like to play?')
            music = takeCommand()
            webbrowser.open(f'https://open.spotify.com/search/{music}')
               
        elif 'weather' in query:
            speak("sure, where would you like to know the weather")
            city = takeCommand()
            weather_info = get_weather(city)
            speak(weather_info)
        
        elif "name" in query.lower():
            speak("My name is " + bot_name + ", I am an AI. What's yours?")
            username = takeCommand()
            speak("Nice to meet you " + username + ". How may I help you?")
        
        elif 'play video' in query.lower():
            speak('What video would you like to watch?')
            video = takeCommand()
            url = f'https://www.youtube.com/results?search_query={video}'
            webbrowser.open(url)
            
        elif 'open spotify' in query.lower():
            speak('Okay. What song would you like to play?')
            music = takeCommand()
            webbrowser.open(f'https://open.spotify.com/search/{music}')
            
        elif 'created you' in query.lower():
            response1 = 'SyberTek who is a programmer, He is known as Nartey Mawunyo Kofi-Ackam.'
            speak(response1)
            
        elif "open browser" in query.lower():
            webbrowser.open("https://www.google.com")
       
        elif "open instagram" in query.lower():
            webbrowser.open("https://www.instagram.com")

        elif "open facebook" in query.lower():
            webbrowser.open("https://www.facebook.com")

        elif "open chatgpt" in query.lower():
            webbrowser.open("https://chat.openai.com/?model=gpt-3.5-turbo-render-sha")
            continue

        elif "open youtube" in query.lower():
            webbrowser.open("https://www.youtube.com/")
            continue

        elif "open discord" in query.lower():
            webbrowser.open("https://discord.com/channels/@me")

        elif "open tiktok" in query.lower():
            webbrowser.open("https://www.titok.com")

        elif "check my mail" in query.lower():
            webbrowser.open("https://www.gmail.com")

        elif "genisys open code" in query.lower():
            webbrowser.open("https://vscode.dev/")
            
        elif "what is the full meaning of genisys" in query.lower():
            speak('Genisys is a term for an artificial intelligence (AI) system and is short for '
                                            '"Generative Networked Intelligent Systems" or "Genious System". This AI '
                                            'system can be used in areas'
                                            'such as autonomous robotics, computer vision, natural language processing, and'
                                            'machine learning. It typically involves using advanced analytics and '
                                            'algorithms'
                                            'to identify patterns in data and then make predictions or decisions based on '
                                            'those'
                                            ' patterns.')
            
        elif 'offline' in query:
            speak("Goodbye, Have a great day!")
            quit()
