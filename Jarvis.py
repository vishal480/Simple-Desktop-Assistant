import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import mail as m

chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning sir')
    elif hour>=12 and hour<16:
        speak('Good Afternoon sir')
    else:
        speak('Good Evening sir')
    speak('Iam Jarvis')
    speak('How may I help you?')
# speak('hi')

def listenCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recogninizing...')
        query=r.recognize_google(audio,language='en-in')
        print('user query:',query)
    except Exception as e:
        print(e)
        print('say that again please...')
        return 'None'
    return query


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(m.email,m.password)
    server.sendmail(m.email,to,content)
    server.close()



if __name__=="__main__":
    wish()
    while True:
        query=listenCommand().lower()
        #Tasks
        if "wikipedia" in query:
            speak('searching wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print('According to wikipedia:',results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.get('chrome').open('youtube.com')
        elif 'play music' in query:
            s="C:\\Users\\Vishal Padala\\Music\\Playlists"
            music=os.listdir(s)
            # print(music[0][0])
            os.startfile(os.path.join(s,music[0]))
        elif 'time' in query:
            time=datetime.datetime.now().strftime('%H:%M:%S')
            speak('the time is',time)
        elif ('email') in query:
            try:
                speak('what should i send?')
                content=listenCommand()
                to='vishalpadala3@gmail.com'
                sendEmail(to,content)
                speak('Email has been sent successfully')
            except Exception as e:
                print(e)
                speak('Could not send mail')
        elif 'exit' in query:
            speak('Have a nice day sir..')
            break

        