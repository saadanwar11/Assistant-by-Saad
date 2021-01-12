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
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'morning' in command:
        print('Good Morning Boss')
        talk('Good Morning Boss')
    elif 'how are you' in command:
        print('I am doing good Boss')
        talk('I am doing good Boss')
    elif 'what is' in command:
        search = command.replace('what is', '')
        talk('showing results for' + command)
        webbrowser.open('https://google.com/?#q=' + command)
    elif 'thank' in command:
        print('Its my pleasure Sir')
        talk('Its my pleasure Sir')


while True:
    run_alexa()
