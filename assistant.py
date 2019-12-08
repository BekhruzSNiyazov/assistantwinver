from os import remove
from time import sleep
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
from subprocess import Popen
from datetime import datetime
from googletrans import Translator
from random import randrange
from datetime import datetime

jokes = ["Why did the hipster burn his mouth on his coffee? Because he drank it before it was cool.", "What is the difference between a well-dressed man on a unicycle and a poorly dressed man on a bicycle? Attire."]

lang = input("Print your language here (en/ru): ")

def speak(text):
    tts = gTTS(text=text, lang=lang)
    filename = "voice.mp3"
    tts.save(filename)
    if lang == "ru":
        print(f"\nАссистент: {text}\n")
    else:
        print(f"\nAssistant: {text}\n")
    playsound(filename)
    remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language=lang)
            if lang == "ru":
                print(f"Вы: {said}")
            else:
                print(f"You: {said}")
        except:
            if lang == "ru":
                print("Извините, но я вас не слышу.")
            else:
                print("Sorry, but I can't hear you.")

    return said

def note(text):
        date = datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"
        Popen(["notepad.exe", file_name])
        with open(file_name, "w") as f:
            f.write(text)

if lang == "ru":
    speak("Чем я могу вам помочь?")

else:
    speak("How can I help you?")

while True:        

    text = get_audio().lower()

    if lang == "en":
            
        if "Russian" in text:
            translator = Translator()
            text = text.split()
            text.remove("in")
            text.remove("russian")
            text = "".join(text)
            translations = translator.translate(text, dest="ru")
            print(translations.text)

        elif "goodbye" in text:
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
            speak("I am an Assistant by Bekhruz Niyazov. I can translate English to Russian, set timers, make notes and I can count!")

        elif "make a note" in text or "write this down" in text or "remember this" in text:
            speak("What would you like to write down?")
            note_text = get_audio()
            note(note_text)
            speak("I've made a note of that.")

        elif text == None:
            sleep(1)

        elif "tell" in text and "joke" in text:
            speak(jokes[randrange(1)])

        elif "what" in text and "time" in text:
            speak(datetime.now())
     
        else:
            speak("Sorry, I didn't understand you.")

        sleep(1)

    elif lang == "ru":

        if "кто ты" in text or "что ты умеешь" in text:
            speak("Я ассистент созданный Ниязовом Бехрузом...")

        else:
            speak("Извините, но я этого еще не умею!")
    else:
        speak("Sorry, but I don't know that language yet!")
