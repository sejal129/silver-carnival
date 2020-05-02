import pyttsx3 #python text to speech module, to install pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia  #pip install wikipedia
import webbrowser
import os #for using system files
import random
import smtplib

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

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("sejalc230@gmail.com","your-password")
    server.sendmail("friend_email@gmail.com",to,content)
    server.close()



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
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open visual studio code' in query:
            code_path="C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path) 

        elif 'send email to friend' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="friend"
                sendEmail(to,content)
                speak("Your email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, couldn't send the email. Try Again!")



