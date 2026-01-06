import speech_recognition as sr
import pyttsx3
import datetime
import os
import subprocess
import pyautogui

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
        print("Speech output not supported.")

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
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.pause_threshold = 1 
        recognizer.energy_threshold = 4000
        
        # WE MUST PUT THE LISTEN LINE INSIDE THE TRY BLOCK
        try:
            audio = recognizer.listen(source, timeout=5) 
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language="en-in")
            print("You said:", command)
            return command.lower()
            
        except sr.WaitTimeoutError:
            # This happens if you don't speak within 5 seconds
            print("Listening timed out.")
            return None
        except sr.UnknownValueError:
            speak("Could not understand audio. Please try again!!")
            return None
        except sr.RequestError:
            speak("Unable to access the Google Speech Recognition API !!")
            return None
        except Exception as e:
            print(f"Something went wrong: {e}")
            return None

def run_assistant():
    wish()

    while True:
        query = listen_command()

        if query is not None:
            if "open e drive" in query:
                # The double backslash \\ is necessary in Python paths
                os.startfile("E:\\")
                speak("Opening your E disk.")
            
            elif 'open my projects' in query:
                # Give the project file path to the variable
                project_path = "E:\\Project Py - VS"
                os.startfile(project_path) #By using startfile we can open files
                speak("Opening the project folder.")
            
            elif 'what is in this folder' in query:
                path = "E:\\Project Py - VS"
                #By using listdir we can list the things inside a folder
                files = os.listdir(path)
                speak(f"Inside this folder, I found {len(files)} items.")
                if len(files) >= 5:
                    # Speak the first 5 files so it doesn't take too long
                    for file in files[:5]:
                        print(file)
                        speak(file)
                else:
                    for file in files:
                        print(file)
                        speak(file)
            
            elif 'close this window' in query:
                speak("Closing the current window.")
                pyautogui.hotkey('alt', 'f4')

            elif 'open notepad' in query:
                speak("Opening Notepad.")
                # subprocess.Popen is better than os.system because it 
                # doesn't wait for you to close notepad before continuing the script
                subprocess.Popen('notepad.exe')
            
            elif 'open calculator' in query:
                speak("Opening Calculator.")
                subprocess.Popen('calc.exe')
            
            elif 'close notepad' in query:
                speak('Closing Notepad.')
                os.system("taskkill /f /im notepad.exe") #By using taskkill we closed the specific application
            
            elif 'close calculator' in query:
                speak('Closing Calculator.')
                os.system("taskkill /f /im calc.exe")
                os.system("taskkill /f /im CalculatorApp.exe")
            
            elif 'shutdown' in query:
                speak("Warning: This will turn off the computer. Do you want to proceed?")
                confirm = listen_command()
                if 'yes' in confirm:
                    os.system("shutdown /s /t 5") # 5 second delay
                else:
                    speak("Shutdown cancelled.")
            

            elif 'stop' in query or 'exit' in query or 'bye' in query:
                speak("Goodbye!")
                break

            else:
                speak("Sorry I didn't have that command!!:(")

run_assistant()
