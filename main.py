import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #voice[0] male

def talk(text):
    engine.say(text)
    engine.runAndWait()
    engine.say('Hello. I am alex.')
    engine.say('How can I help you')

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alex' in command:
                command = command.replace('alex', '')
                print(command)
    except:
        pass
    return command


def run_alex():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current Time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)


    elif 'friend' in command:
        talk('okay sure')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'are you there' in command:
        talk('Yep. Sup')
    else:
        talk('Im sorry I didnt get that')


run_alex()
