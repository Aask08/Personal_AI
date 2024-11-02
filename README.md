##Leo: The Personal Voice Assistant

Leo is an advanced Python-based AI voice assistant designed to help users streamline tasks, automate workflows, and access quick responses by voice commands. Created with a modular structure, Leo offers an extensive range of features, including web searches, system management, real-time data, and personalized reminders, making it a versatile and customizable assistant for everyday use.

#Features

Leo is packed with various functionalities to cover a wide range of tasks:

Web Searches: Use voice commands to search Google, YouTube, and Wikipedia directly.
System Commands: Open and close applications, shut down the system, adjust volume, and more.
Real-Time Information: Get the current time, weather in Bhubaneswar, and check internet speed.
Interactive Features: Play games like Rock-Paper-Scissors, manage personal reminders, and recall saved information.
Media Controls: Control YouTube playback, set volume levels, and adjust playback speed.
Additional Capabilities: Hotword detection ("Leo"), voice output at each interaction, Google translation, scheduling, GUI options, and more.
#Modules
Leo’s code is structured into modules, each dedicated to a specific function, making the assistant flexible and easy to extend.

Module	Description

core_utils.py	- Core functions for speaking, listening, and hotword detection.
greet.py- Manages initial greetings and conversational responses.
web_search.py	- Web search functionalities for Google, YouTube, and Wikipedia.
temperature.py	- Retrieves real-time weather information for Bhubaneswar.
app_management.py	- Opens and closes specified system applications.
youtube_control.py	- Controls YouTube playback with commands like play, pause, forward, backward, etc.
memory.py -	Allows the assistant to remember and recall notes or user-defined information.
internet_speed.py	- Checks internet download and upload speeds.
game.py	- Plays Rock-Paper-Scissors with the user.
shutdown.py	- Provides a command to shut down the system.
Each module can be easily modified or extended to add more functionalities as needed.

#Requirements

Leo requires the following Python packages:

pyttsx3	            -Text-to-speech conversion for voice feedback.
SpeechRecognition	  -Converts speech to text for voice commands.
speedtest-cli	      -Tests internet speed (download/upload rates).
requests	          -Makes API requests to fetch data (e.g., weather).
datetime	          -Handles current date and time manipulation.
wikipedia	          -Accesses Wikipedia articles and summaries.
webbrowser	        -Opens URLs in a web browser.
pywhatkit	          -Automates WhatsApp messaging and Google searches.
random	            -Generates random numbers and selections.
BeautifulSoup	      -Parses HTML/XML documents for web scraping.
os	                -Interacts with the operating system (file handling).


Usage

After starting Leo, you can use voice commands to interact with the assistant. Here are some example commands:

Web Search: "Search Google for Python programming," "Search YouTube for AI tutorials."
Check Time: "What time is it?"
Temperature: "What's the temperature in Bhubaneswar?"
Application Management: "Open Notepad," "Close Chrome."
YouTube Controls: "Play YouTube video," "Pause," "Forward," "Set volume to 50%."
Memory: "Remember that my password is 1234," "What do you remember about my password?"
Game: "Play Rock-Paper-Scissors with me."
System Shutdown: "Shutdown the system."
Exit: "Exit."
Leo will respond to each command either with an action or a voice message to confirm the task.
