#read the MANUAL first.

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import eng_hindi

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    talk('Hi Saad, what can I do ?')
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'morning' in command:
        print('Good Morning Saad')
        talk('Good Morning Saad')
    elif 'how are you' in command:
        print('I am doing good, Saad')
        talk('I am doing good, Saad')
    elif 'what is' in command:
        search = command.replace('what is', '')
        talk('showing results for' + command)
        webbrowser.open('https://google.com/?#q=' + command)
    elif 'who is' in command:
        person = command.replace('who is', '')
        talk('showing results for' + command)
        webbrowser.open('https://google.com/?#q=' + command)
    elif 'thank' in command:
        print('Its my pleasure Saad')
        talk('Its my pleasure Saad')

        
while True:
    run_alexa()
