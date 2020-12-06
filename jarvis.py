import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # it takes microphone input from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sk.a.hakeem123@gmail.com','AFREENshaik@1432')
    server.sendmail('sk.a.hakeem123@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()
    
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('opening youtube...')

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('opening google...')

        elif 'open netflix' in query:
            webbrowser.open("netflix.com/in")
            speak('I think you r in entertainment Mood! just a movement i will open Netflix for you ...')

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
            speak('opening Whatsapp Web...')

        
        

        # system applications
        elif 'play music' in query:
            music_dir = 'D:\\Hacking\\music files\\best music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, Now the time is {strTime}")

        elif 'open telegram' in query:
            codePath = "C:\\Users\\skaha\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(codePath)
            speak('Opening Telegram! please wait')

        elif 'open vlc' in query:
            codePath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(codePath)
            speak('opening vlc media player! please wait')
        
        elif '360' in query:
            codePath = "D:\\"
            os.startfile(codePath)
            speak('opening Hakeem360 Drive! please wait')

        # fun commands
        elif 'who are you' in query:
            speak('i''m your assestent sir!')
        elif 'where are you born' in query:
            speak("i born from your thougts sir!")
        elif 'where are you from' in query:
            speak('i''m from internet! you made me sir! did you forgot about it? i feel very bad!')
        
        elif 'i love you' in query:
            speak('i love you too ! but i''m not a human ! so you have to think about it')
        elif 'shit' in query:
            speak('don''t feel bad dear!')
        
        elif 'f*** you' in query:
            speak('go and! fuck your self first')

        
        elif 'email to anu' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "annapurnaksla@gmail.com"
                sendEmail(to, content)
                speak("email sent successfully!")
                print("email sent successfully")
            except Exception as e:
                print(e)
                speak("errors occured")

        elif 'good job' in query:
            speak("Thank you very much sir")


        

