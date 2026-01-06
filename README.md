### 🎙️ Python Multi-Utility Voice Assistant
## 🌟 Project Overview
  This project is a Desktop Voice Assistant built using Python. It acts as a bridge between the user and the computer, allowing for hands-free interaction with the web, system applications, and the local file system.

The assistant follows a Listen-Process-Act logic:

  * **Listen:** Captures audio via the microphone.
  * **Process:** Converts audio to text and identifies keywords.
  * **Act:** Executes the corresponding Python function (web search, app launch, etc.).

## 🚀 Implementation Use Cases
I have implemented three distinct modules to showcase the assistant's versatility:

  1. **Information Retrieval (Wikipedia)**
    The assistant connects to the Wikipedia API to fetch summaries of any topic. It is designed to provide quick "at-a-glance" information without the user needing to open a browser and read through pages of text.
  
  2. **System & Folder Management**
    This module allows the user to navigate the Windows file system. It can open specific drives (E: or D:), navigate to project folders, and list files. It also manages system power states (Shutdown/Restart).
  
  3. **Desktop Automation**
    Automates the opening and closing of standard Windows applications like Notepad and Calculator. It uses process management to ensure the assistant remains active even while other apps are running.

### 📦 Libraries Used & Their Purpose

| Library | Purpose |
| :--- | :--- |
| `speech_recognition` | The "Ears" of the assistant. It converts spoken audio into a string of text using Google's speech engine. |
| `pyttsx3` | The "Voice" of the assistant. It is a text-to-speech library that works offline and allows for gender/rate customization. |
| `os` | Used for interacting with the Operating System (opening drives, listing files, and system shutdown). |
| `subprocess` | Used to launch system applications (like Notepad) as independent processes. |
| `pyautogui` | A GUI automation tool used to simulate keyboard shortcuts (like `Alt+F4` to close windows). |
| `datetime` | Allows the assistant to know the current time to provide context-aware greetings. |
| `wikipedia` | Connects the assistant to the Wikipedia API for information retrieval. |

## 🗣️ Command Reference
Once you run the code, you can use the following voice commands:

**Web & Info:**

  * "Search Wikipedia for [Topic]" — Fetches a 2-sentence summary from Wikipedia.
  * "Open Google" or "Open YouTube" — Launches the browser to the respective site.

**System Navigation:**

  * "Open E Drive" — Opens the E: partition in File Explorer.
  * "Open my projects" — Navigates directly to your designated project folder.
  * "What is in this folder" — Lists the first 5 files in the current directory.

**Application Control:**

  * "Open Notepad" / "Close Notepad" — Launches or force-closes Notepad.
  * "Open Calculator" / "Close Calculator" — Launches or force-closes the Calculator.
  * "Close this window" — Simulates Alt+F4 to close the active app.

**Power Commands:**

  * "Shutdown" — Asks for confirmation before turning off the PC.
  * "Restart the system" — Reboots the computer after a 10-second delay.

## 🖥️ Requirements for VS Code
To run this project successfully on your local machine using VS Code, ensure the following:

  * Python 3.x Installed: Download from python.org.
  * Virtual Environment (Recommended): Create one to keep your dependencies isolated.
  
  ``Bash
  python -m venv venv
  .\venv\Scripts\activate``
  
  * Microphone Access: Ensure VS Code and Python have permission to access your system's microphone.
  * Internet Connection: Required for the speech_recognition (Google API) and wikipedia modules.
  * Pip Installations:
  
  ``Bash
  pip install SpeechRecognition pyttsx3 pyautogui wikipedia``
  
  (Note: If PyAudio fails on Windows, download the specific .whl file for your Python version.)

## 🎓 Learning Outcomes
Through this project, I have gained hands-on experience in:

  * API Integration: Learned how to connect a Python application to external services like Google Speech and Wikipedia.
  * Process Management: Understanding how to launch and terminate system applications using os and subprocess.
  * Automation: Using pyautogui to bridge the gap between software and hardware through keyboard/mouse simulation.
  * Error Handling: Implementing robust try-except blocks to manage real-world issues like network timeouts and ambient noise.

## 🌟 Project Conclusion
  This Voice Assistant project has been a significant milestone in my journey as a Python developer. It demonstrates the power of automation and how a few lines of code can make human-computer interaction more natural and efficient. Moving forward, I plan to integrate Large Language Models (LLMs) to make the assistant even more intuitive.
