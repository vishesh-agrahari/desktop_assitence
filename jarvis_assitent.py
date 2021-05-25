import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import time
import datetime

engine = pyttsx3.init()
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("good morning sir!")
    elif(hour>=12 and hour<18):
        speak("good afternoon sir!")
    else:
        speak("good evening sir!")
    speak("I am Alexa!! how may i help you")

def takecommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold = 3000
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please...")
        exit()

    return query
def check_query(query):
    if 'wikipedia' in query:
        speak('searching wikipedia')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
        query_again()
    elif 'open youtube' in query:
        webbrowser.open('youtube.com')
    elif 'open google' in query:
        webbrowser.open('google.com')
    elif 'play music' in query:
        music_dir = 'D:\\NEW SONG'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[random.randint(0, 15)]))
    elif 'time' in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        print(time)
        speak(f" sir, the time is {time}")
        query_again()
    elif 'about yourself' in query:
         print("my name is alexa and i am created by sir vishesh agrahari!! how can i help you..")
         speak("my name is alexa and i am created by sir vishesh agrahari!! how can i help you..")
         query_again()
    else:
        print("ok! thank you")
        speak("ok! thank you")
        exit()




def query_again():
    time.sleep(2)
    print("would you like any more help from me..?")
    speak("would you like any more help from me..?")
    query = takecommand().lower()
    if 'no' in query:
        print("ok! thank you")
        speak("ok! thank you")
        exit()
    else:
       check_query(query)

if __name__ == '__main__':
    wishme()
    query = takecommand().lower()
    check_query(query)






