import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    

if __name__ == "__main__":
    speak("Initializing Robo >>>")
    while True:
        # Listen for wake word Morphus
        # Obtain audio from the microphone
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "robo"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("ai Activated....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
        except KeyboardInterrupt:
            continue
