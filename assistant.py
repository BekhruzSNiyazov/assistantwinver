from time import sleep, ctime
from subprocess import Popen
from random import randrange
from os import remove

jokes = ["Why did the hipster burn his mouth on his coffee? Because he drank it before it was cool.", "What is the difference between a well-dressed man on a unicycle and a poorly dressed man on a bicycle? Attire."]
rujokes = ["- Запомни, умный человек всегда во всём сомневается.\nТолько дурак может быть полностью уверенным в чём-то.\n- Ты уверен в этом?\n- Абсолютно.", "— Скажите, какова ваша методика написания диплома?\n— Crtl C, Ctrl V!", "Утром мать спрашивает дочь:\n- Что ночью упало с таким грохотом?\n- Одежда\n- А почему так громко?\n- Я не успела из нее вылезти...", "На чемпионате мира по плаванию тройку лидеров замкнул электрик Петров."]
hello = ["Hello to you to!", "Hi!", "Hi, how can I help you?", "Hello, how can I help you?", "Hi! How are you?", "How can I help you?", "How can I help?"]
goodbye = ["Goodbye to you to!", "See you later!", "Hope, I'll see you again!", "Waiting for help!"]
sorry = ["Sorry, I can't do that yet!", "Sorry, but I don't understand that!", "Sorry, I can't do that yet! Please, try another command."]
feeling = ["I'm fine, thank you!", "Very well, thanks!", "Very good, tank you! And you?"]
bad = [f"Why are you so {feeling}?", "What's wrong?", "What can I do for you?", "If you want to, I can make you laugh. Just say: \"Make me laugh.\""]
thanks = ["Glad you like it.", "You are welcome."]


lang = ""

try:
    f = open("info.txt", "r")
    lang = f.read()
except:
    lang = input("Print your language here (en/ru): ")
    f = open("info.txt", "w")
    f.write(lang)

def speak(text):
    print(text)

def get_audio():
    return input()

def note(text):
        date = ctime()
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
        if "remember" in text:
            speak("What do I need to remember?")
            global info
            info = get_audio()

        elif "you" in text and "remember" in text:
            speak(info)

        elif "goodbye" in text:
            speak(goodbye[randrange(len(goodbye))])

        elif "stop" in text:
            break

        elif "ha" in text or "thank you" in text or "thanks" in text:
            speak(thanks[randrange(len(thanks))])

        elif "change" in text and "language" in text:
            speak("Which language whould you like to use?")
            lang = input("Plaese, type the language here (en/ru): ")
            f = open("info.txt", "w")
            f.write(lang)
            speak("Successfully changed!")

        elif "hello" in text:
            speak(hello[randrange(len(hello))])

        elif "what is your name" in text:
            speak("My name is Assistant")
        elif "thank you" in text:
            speak("You are welcome!")

        elif "how are you" in text:
            speak(feeling[randrange(len(feeling))])

        elif "i am" in text:
            feeling = ""
            if "bad" in text or "angry" in text:
                if "bad" in text:
                    feeling = "bad"
                else:
                    feeling = "angry"
                speak(bad[randrange(len(bad))])

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
            
        elif "timer" in text:
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
            try:
                note(note_text)
                speak("I've made a note of that.")
            except:
                speak(sorry[randrange(len(sorry))])

        elif text == None:
            sleep(1)

        elif "joke" in text or "laugh" in text:
            speak(jokes[randrange(len(jokes))])

        elif "time" in text:
            speak(ctime())

        elif "date" in text:
            print(ctime())

        elif "say" in text or "speak" in text:
            words = input('Please, write what I have to say.')
            speak(words)

        elif "open" in text:
            Popen([f"{text.split()[-1]}.exe", ""])

        else:
            speak(sorry[randrange(len(sorry))])

        sleep(1)

    elif lang == "ru":
        try:
            if "кто ты" in text or "что ты умеешь" in text or "кто тебя создал" in text:
                speak("Я ассистент созданный Ниязовом Бехрузом и Петром Репьевым. Я могу говорить время и дату, шутить, делать заметки и многое другого")

            elif "дата" in text: 
                print(ctime())

            elif "пока" in text or "до свидания" in text or "прощай" in text:
                    speak("Пока! Скажите стоп, чтоб прекратить работу.")

            elif "стоп" in text:
                break

            elif "время" in text or "времени" in text:
                speak(ctime())

            elif "шутка" in text or "шутку" in text or "пошути" in text:
                speak(rujokes[randrange(len(rujokes))])

            elif "таймер" in text:
                speak("Пожалуйста, напишите количество секунд на которое поставить таймер.")
                tr = int(input())
                speak("Установлено!")
                sleep(tr)
                speak("Время истекло!")

            elif "сделай заметку" in text or "напиши это" in text or "запомни это" in text:
                speak("Что мне нужно запомнить?")
                note_text = get_audio()
                note(note_text)
                speak("Я это записал.")

            elif text == None:
                sleep(1)

            elif "запомни" in text:
                speak("Что я должен запомнить?")
                global info2
                info2 = get_audio()

            elif "ты" in text or "вы" in text and "запомнил" in text or "запомнила" in text:
                speak(info)

            elif "привет" in text:
                speak("Тебе привет тоже!")

            elif "как тебя зовут" in text:
                speak("Меня зовут ...")

            elif "спасибо" in text:
                speak("Не за что!")

            elif "как ты" in text:
                speak("Хорошо, спасибо!")

            elif "случайное число" in text:
                i2 = randrange(100)
                speak(i2)

            elif "произнеси" in text or "скажи" in text:
                words = input('Пожалуйста, напишите, что мне надо произнести.')
                say(words)

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

            else:
                speak("Извините, но я этого еще не умею!")

        except:
            speak("Извините, но я не могу сейчас выполнить эту команду, повторите попозже.")

    else:
        speak("Sorry, but I don't know that language yet! Извините, но я ещё не знаю этого языка!")
