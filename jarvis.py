import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices =  engine.getProperty('voices')
#print(voices[0])
engine.setProperty('voice', voices[0].id)

def wishme():
    hour =  int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING")
    elif hour>=12 and hour>=18:
        speak("GOOD AFTERNOON")
    else:
        speak("GOOD EVENING")
    speak("I am Jarvis mam, please tell me how may I help you?")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
       
    try:
        print("Recoginizing...")
        query = r.recognize_google(audio, language='en-US')
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
    server.login('your_email@gmail.com', 'your_password')
    server.sendmail('your_email@gmail.com', to, content)
    server.close()
    

if __name__ == "__main__":
    wishme()
    
    while True:
        query1 = takeCommand().lower()

        if "tell me about" in query1:
            speak("Searching Wikipedia...")
            query1 = query1.replace("tell me about", "")
            results = wikipedia.summary(query1, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif "Hello Jarvis" in query1:
            speak("Hello Mam, tell me what do you want me to do?")

        elif "open youtube" in query1:
            webbrowser.open("youtube.com")

        elif "open google" in query1:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query1:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query1:
            music_dir = "D:\\Entertainment\\desktop\\Music\\Music (2)\\Sample Music"
            songs =  os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
    
        elif "the time" in query1:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Mam, the time is {Time}")

        elif "the code" in query1:
            codepath = "C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codepath)

        elif 'email to the_name' in query:
            try:
                speak("What should I say?")
                content =  takeCommand()
                to = "the_email@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry Mam, I am not able to send this email at this moment.")



       