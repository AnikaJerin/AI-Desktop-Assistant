import pyttsx3
import datetime
import speech_recognition as sr #The primary purpose of a Recognizer instance is, of course,
# to recognize speech. Each instance comes with a variety of settings and functionality for recognizing speech from an
# audio source.
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
'''pyttsx3.init([driverName : string, debug : bool]) → pyttsx3.Engine
Gets a reference to an engine instance that will use the given driver.
If the requested driver is already in use by another engine instance, that engine is returned. Otherwise,
a new engine is created.The Speech Application Programming Interface or SAPI is an API developed 
by Microsoft to allow the use of speech recognition and speech synthesis within Windows applications.'''
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    '''declaring speak function and passing audio argument which will be pronounced by the assistant'''
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hi! I am your voice assistant for today! How may I help you?")

def takecommand():
    '''It takes microphone input from the user and return it as a string output'''
    r= sr.Recognizer() #class speech recognition er. Creating a Recognizer instance is easy.
    #Each Recognizer instance has seven methods for recognizing speech from an audio source using various APIs
    with sr.Microphone() as source:
        #use the default microphone as the audio source
        print("Listening...")
        r.pause_threshold=1 #instance attribute of speech recognition
        audio=r.listen(source) #listen for the first phrase and extract it into audio data
        #commented out by Syeda anika Jerin to understand this program easily
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in') # recognizer_instance.recognize_google(audio_data, key = None,
        # language = "en-US", show_all = False)
        # Performs speech recognition on audio_data (an AudioData instance), using the Google Speech Recognition API.
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e) # commented   out so that error doesn't show in console
        print("Say Again")
        return "None" #None string returs
    return query

def sendemail(to,content):
    #you have to enable less secure apps from your gmail and import smtplib that helps to send emails
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() #Identify yourself to an ESMTP server using EHLO.
    # The hostname argument defaults to the fully qualified domain name of the local host.
    server.starttls() #Put the SMTP connection in TLS (Transport Layer Security) mode.
    # All SMTP commands that follow will be encrypted. You should then call ehlo() again.
    server.login('youremail@gmail.com','yourpassword')#try to put your password in a text file and import here
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wish()
    if 1:
        query=takecommand().lower() #converting our comand query in lower case for convenience.otherwise we have to write 'open..'
        # in capital letters
        #Logic for executing tasks based on query
        if 'wikipedia'in query:
            speak("Searching wikipedia keep Patience")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2) #read 2 sentences from requested wikipedia article
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            #when user say like open youtube then query'll be true for open youtube
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'play music' in query:
            music_dr='G:\\download 3\\Music' #double backslash is escaping characters
            songs=os.listdir(music_dr) #lists all the files under music_dr directory
            print(songs)
            os.startfile(os.path.join(music_dr,songs[0]))  #can use random modeule to generate random number. then your assistant
            #can play random songs
        elif 'what time' in query:
            strtime=datetime.datetime.now().strftime("%H hour %M minute %S seconds")
            print(strtime)
            speak(f"The time is{strtime}")

        elif 'email to ani' in query:
            #we are taking only anika as input but we can import all contacts from gmail create a dictionary at the start of the code
            #where keys would be the name of users and values would be mail ids
            try:
                speak("What should I write in the content")
                content=takecommand()#this function take audio that you say as input and return it as a string
                to="emailaddress of whom you want to send email@gmail.com"
                sendemail(to,content)
                speak("Your email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry your email couldnot be sent")
