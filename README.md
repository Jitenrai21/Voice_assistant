Jarvis AI 🤖
Jarvis AI is a Python-based voice-commanded virtual assistant that uses speech recognition and text-to-speech to interact with users. It responds to voice commands, opens websites, tells jokes, provides the current time, and more. Built with libraries like speech_recognition, pyttsx3, and pyjokes, Jarvis AI is your personal assistant inspired by the iconic JARVIS from Iron Man. 🚀
Features ✨

Speech Recognition: Converts spoken words to text using Google's Speech Recognition API. 🎙️
Text-to-Speech: Outputs responses in a robotic voice with customizable speech rate. 🗣️
Wake Word Activation: Responds to the wake word "Jarvis" for hands-free operation. 👂
Website Navigation: Opens predefined websites like YouTube, ChatGPT, and GitHub. 🌐
Time Reporting: Provides the current time in a user-friendly format. ⏰
Joke Telling: Delivers random jokes using the pyjokes library. 😂
Application Launch: Opens applications like Google Chrome. 🖥️
Custom Commands: Supports specific commands like playing a Taylor Swift video. 🎵

Available Commands and Responses 🎉
Jarvis AI responds to voice commands after being activated with the wake word "Jarvis". Below are the supported commands and their responses:

Wake Word ("Jarvis"):

"I am ready for your command."


How Are You (e.g., "How are you"):

"I am doing great, How are you?"


Your Name (e.g., "What's your name"):

"It's so silly for you to ask again. My name is Javis."


Old Are You (e.g., "How old are you"):

"I have been created quite a while ago. By Jiten Rai, of course!"


Time Now (e.g., "What time is it now"):

"The time is [current time in HH:MM AM/PM format]."


Joke (e.g., "Tell me a joke"):

Delivers a random joke, e.g., "Why did the programmer prefer dark mode? Because the light attracts bugs."


Swift (e.g., "Play Swift"):

Opens a specific Taylor Swift YouTube video.


Open Chrome (e.g., "Open Chrome"):

"Opening google chrome."


Exit (e.g., "Exit"):

"I am always at your service. Come again."



Prerequisites 🛠️
To run Jarvis AI, ensure you have the following installed:

Python 3.8+ 🐍
pyttsx3 (pip install pyttsx3) 🗣️
speech_recognition (pip install SpeechRecognition) 🎙️
pyjokes (pip install pyjokes) 😂
A working microphone 🎤
Internet connection for Google Speech Recognition API 🌐
Windows OS for application launching (e.g., Chrome) 💻
Modify paths for other operating systems if needed.



Installation ⚙️

Clone the Repository:
git clone https://github.com/Jitenrai21/Jarvis-AI.git
cd Jarvis-AI


Install Dependencies:
pip install pyttsx3 SpeechRecognition pyjokes


Ensure Microphone Setup:Verify your microphone is connected and functional.


Usage 🚀

Run the Assistant:
python jarvis.py


Interact with Jarvis:

Say "Jarvis" to activate the assistant. 👂
Speak commands like:
"How are you?" → Responds with a friendly reply. 😊
"Tell me a joke" → Shares a random joke. 😂
"What time is it now?" → Provides the current time. ⏰
"Open Chrome" → Launches Google Chrome. 🖥️
"Exit" → Stops the assistant. 🚪


If the wake word is not detected, Jarvis prompts: "Activate by calling me by my name Jarvis."



Project Structure 📁
Jarvis-AI/
│
├── jarvis.py            # Main script to run the voice assistant 🤖
├── README.md            # Project documentation 📖
└── requirements.txt     # List of dependencies 📋

Extending Jarvis AI 🌟

Add New Commands: Modify the command loop in jarvis.py to include new voice triggers and actions. ➕
Support More Websites: Expand the sites list to include additional websites. 🌐
Cross-Platform Compatibility: Update application paths (e.g., Chrome) for macOS or Linux. 💻
Local Music Playback: Uncomment and configure the music playback feature with correct file paths. 🎵
Advanced NLP: Integrate with a chatbot framework for more complex conversations. 🧠

Contributing 🤝
Contributions are welcome! To contribute:

Fork the repository. 🍴
Create a new branch (git checkout -b feature-branch). 🌿
Make your changes and commit (git commit -m "Add feature"). 💾
Push to the branch (git push origin feature-branch). 🚀
Open a Pull Request. 📬

License 📜
This project is licensed under the MIT License. See the LICENSE file for details. ✅
Acknowledgments 🙌

Built with pyttsx3 for text-to-speech. 🗣️
Uses SpeechRecognition for voice input. 🎙️
Powered by pyjokes for humor. 😂
Inspired by JARVIS from Iron Man and open-source voice assistants. 🌍


For any issues or questions, please open an issue on the GitHub repository. 🐛
