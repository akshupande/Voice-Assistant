import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_name():
    talk("Hi, what's your name?")
    name = take_command()
    return name


def take_command():
    try:
        with sr.Microphone() as data_taker:
            print("Say Something")
            voice = listener.listen(data_taker)
            instruct = listener.recognize_google(voice)
            instruct = instruct.lower()
            if 'max' in instruct:
                instruct = instruct.replace('max', '')
                print(instruct)
    except sr.RequestError:
        talk("Sorry, I couldn't connect to the internet.")
    except sr.UnknownValueError:
        talk("Sorry, I didn't understand what you said.")
    return instruct


def run_max():
    name = get_name()
    talk(f"Hi, {name}, how can I help you?")
    while True:
        instruct = take_command()
        if 'play' in instruct:
            song = instruct.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in instruct:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('The current time is ' + time)
        elif 'tell me about' in instruct:
            thing = instruct.replace('tell me about', '')
            info = wikipedia.summary(thing, 2)
            print(info)
            talk(info)
        elif 'who are you' in instruct:
            talk('I am your personal assistant Max.')
        elif 'what can you do for me' in instruct:
            talk('I can play songs, tell time, and help you with Wikipedia.')
        elif 'stop' in instruct:
            talk('Goodbye!')
            break
        else:
            talk("Sorry, I didn't understand what you said. Can you repeat that?")

run_max()
