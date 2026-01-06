import speech_recognition as sr
import datetime
import webbrowser
import pyautogui
import pyttsx3
import time

def speak(text):
    try:
        print("Assistant:",text)
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
        print("Speech Output not supported!")

def wish():
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
    recognize = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening Command...")
        recognize.pause_threshold = 1
        recognize.energy_threshold = 4000
        audio = recognize.listen(source, timeout = 5)
    
    try:
        command = recognize.recognize_google(audio, language = "en-in")
        print("You said:",command)
        return command.lower()
    # Handling Exceptional errors
    except sr.UnknownValueError:
        speak("Could not understand audio. Please try again!!")
        return None
    except sr.RequestError:
        speak("Unable to access the Google Speech Recognition API!!")
        return None
    except sr.WaitTimeoutError:
        speak("Times up!! Please try again!")
        return None
    
def run_assistant():
    wish()

    while True:
        query = listen_command()

        if query is not None:
            if 'open youtube' in query:
                speak('Opening Youtube!')
                webbrowser.open("http://youtube.com")
                time.sleep(5)
            
            elif 'search' in query and 'youtube' in query:
                speak("What should I search for?")
                search_data = listen_command()
                if search_data is not None:
                    # This opens the search results page directly
                    webbrowser.open(f"https://www.youtube.com/results?search_query={search_data}")
                    speak(f"Here are the search results for {search_data}")
                    time.sleep(2)
                    pyautogui.click(700, 400) # Clicks the center of a 1080p screen
                    time.sleep(2)
            
            elif 'pause' in query or 'play' in query:
                # YouTube uses 'k' to toggle play/pause reliably
                pyautogui.press('k')
                speak("Done.")

            elif 'mute' in query:
                pyautogui.press('m')
                speak('Done')

            elif 'volume up' in query:
                # Pressing the 'up' arrow key increases volume
                pyautogui.press('up')
                speak('Done')

            elif 'volume down' in query:
                pyautogui.press('down')
                speak('Done')

            elif 'scroll down' in query:
                # We can use the 'space' or 'pagedown' key or axis coordinates to scroll down
                pyautogui.scroll(-500)
            
            elif 'scroll up' in query:
                # We can use the 'pageup' key or axis coordinates to scroll up
                pyautogui.scroll(500)

            elif 'next tab' in query:
                # Switch between open tabs in Chrome/Edge
                pyautogui.hotkey('ctrl', 'tab')

            elif 'close this tab' in query:
                # Instantly closes the current tab
                pyautogui.hotkey('ctrl', 'w')
                speak("Tab closed.")
            
            elif 'exit' in query or 'bye' in query:
                speak("GoodBye!! Have a nice day!")
                break

            else:
                speak("Sorry I didn't have that command.")

        else:
            break

run_assistant()
