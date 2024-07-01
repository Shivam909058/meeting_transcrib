# lets create a model which converts sppech into text and saves it in a file

import speech_recognition as sr
import os

# so we are going to use microphone as our source kuyki meeting mai microphone se hi baat hoti hai
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source)
    print("Time over, thanks")

try:
    print("TEXT: "+r.recognize_google(audio))
    with open("speech.txt", "w") as file:
        file.write(r.recognize_google(audio))
except:
    pass


