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

rujokes = ["- Запомни, умный человек всегда во всём сомневается.\nТолько дурак может быть полностью уверенным в чём-то.\n- Ты уверен в этом?\n- Абсолютно.", "— Скажите, какова ваша методика написания диплома?\n— Crtl C, Ctrl V!",
"Утром мать спрашивает дочь:\n- Что ночью упало с таким грохотом?\n- Одежда\n- А почему так громко?\n- Я не успела из нее вылезти...", "На чемпионате мира по плаванию тройку лидеров замкнул электрик Петров."]

lang = input("Print your language here (en/ru): ")

def speak(text):
    try:
        tts = gTTS(text=text, lang=lang)
        filename = "voice.mp3"
        tts.save(filename)
        if lang == "ru":
            print(f"\nАссистент: {text}\n")
        else:
            print(f"\nAssistant: {text}\n")
        playsound(filename)
        remove(filename)
    except:
        print("error")

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
            speak("I am an Assistant by Bekhruz Niyazov and Peter Repiev. I can translate English to Russian, set timers, make notes and I can count!")

        elif "make a note" in text or "write this down" in text or "remember this" in text:
            speak("What would you like to write down?")
            note_text = get_audio()
            note(note_text)
            speak("I've made a note of that.")

        elif text == None:
            sleep(1)

        elif "tell" in text and "joke" in text:
            speak(jokes[randrange(len(jokes))])

        elif "what" in text and "time" in text:
            speak(datetime.now())

        elif 'date' in text:
            import datetime 
            print(datetime.date.today())
     
        else:
            speak("Sorry, I didn't understand you. ")

        sleep(1)

    elif lang == "ru":
        try:
            if "кто ты" in text or "что ты умеешь" in text or "кто тебя создал" in text:
                speak("Я ассистент созданный Ниязовом Бехрузом и Петром Репьевым в декабре 2019. Я могу говорить время и дату, шутить,\n делать заметки и много другого")

            elif 'дата' in text:
                import datetime 
                print(datetime.date.today())

            elif "пока" in text or "до свидания" in text or "прощай" in text:
                    speak("Пока! Скажите стоп, чтоб прекратить работу.")

            elif "стоп" in text:
                break

            elif "время" in text or "времени" in text:
                speak(datetime.now())

            elif "шутка" in text or "шутку" in text or "пошути" in text:
                speak(rujokes[randrange(len(rujokes))])

            else:
                speak("Извините, но я этого еще не умею!")
        except:
            speak("Извините, но я не могу сейчас выполнить эту команду, повторите попозже.")

    else:
        speak("Sorry, but I don't know that language yet! Извините, но я ещё не знаю этого языка!")
