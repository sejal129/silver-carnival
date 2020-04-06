import pyttsx3 #python text to speech module, to install pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia  #pip install wikipedia
import webbrowser
import os #for using system files
import random

#print(sr.__version__)
engine = pyttsx3.init('sapi5') # sapi5 is a driver for windows
voices= engine.getProperty('voices')

#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

# speak function will convert text to speech
def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
     

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Bruv. Please tell me how may I help you?")

#function to take microphone input commands 
def takeCommand():
    #It takes microphone input from the user and returns string output
    r=sr.Recognizer() #Recognizer class object
    with sr.Microphone() as source: #context manager
        print("Listening..")
        #r.pause_threshold = 1
        r.adjust_for_ambient_noise(source) #reduce unwanted noise 
        audio = r.listen(source)
        #listen functio will listen to our commmand(input)
        #print(audio) 

    try:
        print("Recognizing..")
        query=r.recognize_google(audio, language="en-in") #using google engine to recognize
        print(f"User said: {query}\n") #fstring
        #speak(query)
 
    except Exception:
        print("Please say again..")
        query= None

    return query

#Main program
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia..")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2) #Give summary of the query in 2 lines
            speak("According to Wikipedia")
            #print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")

        elif 'play music' in query:
            music_dir="C:\\Users\\Admin\\Music\\Songs"
            songs=os.listdir(music_dir)
            #print(songs)
            r=random.randint(0,len(songs)-1) #generate random song from the list
            os.startfile(os.path.join(music_dir,songs[r]))

        


