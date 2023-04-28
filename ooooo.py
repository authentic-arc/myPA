import speech_recognition
import pyttsx3
import datetime
import pyjokes
import pywhatkit

engine = pyttsx3.init()
engine.say('Sally sells seashells by the seashore.')
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

listen = speech_recognition.Recognizer()

def commm():
    try:
        with speech_recognition.Microphone() as source:
            print("sure")