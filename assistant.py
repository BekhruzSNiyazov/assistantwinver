from os import remove
from time import sleep
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
from subprocess import Popen
from datetime import datetime
from random import randrange

jokes = ["Why did the hipster burn his mouth on his coffee? Because he drank it before it was cool.", "What is the difference between a well-dressed man on a unicycle and a poorly dressed man on a bicycle? Attire."]

def speak(text):
    tts = gTTS(text=text, lang="en")
    file = "audio.mp3"
    tts.save(file)
    playsound(file)
    print(f"\nAssistant: {text}\n")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(f"You: {said}")
        except Exception as e:
            print("Exception: " + str(e))

    return said

def note(text):
        date = datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"
        Popen(["notepad.exe", file_name])
        with open(file_name, "w") as f:
            f.write(text)

speak("How can I help you?")

while True:        

    text = get_audio()
        
    if "goodbye" in text:
    	speak("Goodbye to you to! Say stop to stop.")

    elif "stop" in text:
        break

    elif "hello" in text:
        speak("Hello to you to!")

    elif "what is your name" in text:
        speak("My name is Assistant")
    elif "thank you" in text:
        speak("You are welcome!")

    elif "how are you" in text:
        speak("I'm fine, thank you!")

    elif "random number generator" in text:
        i = randrange(100)
        speak(i)

    elif "+" in text:
        text = text.split()
        speak(f"{text[0]} + {text[-1]} = {text[0] + text[-1]}")

    elif "-" in text:
        text = text.split()
        speak(f"{text[0]} - {text[-1]} = {text[0] - text[-1]}")

    elif "*" in text:
        text = text.split()
        speak(f"{text[0]} * {text[-1]} = {text[0] * text[-1]}")
        
    elif "/" in text:
        text = text.split()
        speak(f"{text[0]} / {text[-1]} = {text[0] / text[-1]}")   
        
    elif "set" and "timer" in text:
        speak("Please, write the number of seconds to set the timer.")
        t = int(input())
        speak("Started!")
        sleep(t)
        speak("Time over!")

    elif "what can you do" in text:
        speak("I am an Assistant by Bekhruz Niyazov. I can translate English to Russian (Sth in Russian), set timers (set a timer), make notes (make a note, write this down or remember this) and I can count (10 + 10, 20 - 10, 2 * 2, 10 / 2)")

    elif "make a note" in text or "write this down" in text or "remember this" in text:
        speak("What would you like to write down?")
        note_text = get_audio()
        note(note_text)
        speak("I've made a note of that.")

    elif text == None:
        sleep(1)

    elif "tell" in text and "joke" in text:
        speak(jokes[randrange(1)])
 
    else:
        speak("Sorry, I didn't understand you.")

    sleep(1)
