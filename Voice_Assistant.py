import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

def speak(text):
    print(f"Assistant: {text}")
    try:
        # Initialize the python text to speech model
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')#It will fecth the default voices in our system
        engine.setProperty('voice',voices[1].id)#I selected the female tone, by default it will be male
        engine.say(text) #Whatever in the text will be told
        engine.runAndWait()
    except:
        print("Speech output not supported. ")

def wish():
    # Greets the user based on real time
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning.")
    elif hour < 15:
        speak("Good Afternoon.")
    elif hour < 19:
        speak("Good evening.")
    else:
        print("Good night.")
    speak("I am you voice assistant. How can I help you today?")

def listen_command():
    #By using SpeechRecognition we listen the audio from mic
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.pause_threshold = 1 
        recognizer.energy_threshold = 4000
        audio = recognizer.listen(source, timeout = 5) 
    
    try:
        command = recognizer.recognize_google(audio, language = "en-in")
        print("You said:",command)
        return command.lower()
    # Handling Exceptional errors
    except sr.UnknownValueError:
        speak("Could not understand audio. Please try again!!")
        return None
    except sr.RequestError:
        speak("Unable to access the Google Speech Recognition API !!")
        return None
    except sr.WaitTimeoutError:
        speak("Times up!! Please try again!")
        return None

def run_assistant():
    wish()

    while True:
        query = listen_command()
        
        if query is not None:
            # Shows the real time in 24 hours format
            if "time" in query:
                time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The current time is {time}")

            elif "wikipedia" in query:
                # Fetch the details from wikipedia
                query = query.replace("wikipedia","")
                try:
                    print("Searching...")
                    results = wikipedia.summary(query, sentences = 2)
                    speak("According to Wikipedia..")
                    speak(results)
                except:
                    speak("Sorry I can't find that topic!!")

            # Open Google and YouTube
            elif "open youtube" in query:
                speak("Opening You Tube..")
                webbrowser.open("http://youtube.com")

            elif "open google" in query:
                speak("Openning Google..")
                webbrowser.open("http://google.com")

            elif "exit" in query or "bye" in query:
                speak("Goodbye!! Have a nice day!")
                break

            else:
                speak("Sorry I didn't have that command!!:(")
        else:
            break

run_assistant()
