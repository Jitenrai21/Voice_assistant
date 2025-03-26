# Importing all the needed packages
import pyttsx3 # for text to speech(in robotic voice) translation
import speech_recognition as sr # converts spoken words into text
import pyjokes
import webbrowser
import datetime
import os
import time

#This is the function to capture speech and convert to text
def sptext():
    recognizer = sr.Recognizer() #initializa an object of Speech recognizer
    with sr.Microphone() as source: #use mic for input voice
        print("Listening...") #status update for user
        recognizer.adjust_for_ambient_noise(source) #adjusting bg noises
        audio = recognizer.listen(source) #record audio from source
        try:
            print("Recognizing...") #status update
            data = recognizer.recognize_google(audio) #using google speech recognition to convert audio to text
            print(data) #display recognized text
            return data #return text data
        except sr.UnknownValueError: #exception handling
            print("Couldn't understand the message.") #error message
            return sptext() #recursion to let the user try again
        
#This function is to output the comprehended text into speech
def speechtx(x): 
    engine = pyttsx3.init() #initialize text-to-speech engine
    voices = engine.getProperty("voices") #get voice options
    engine.setProperty('voice', voices[0].id) #[0] indicates male voice
    rate = engine.getProperty('rate') #understand current speech rate
    engine.setProperty('rate',150) #set the speech rate to 150 words per minute
    engine.say(x) #queue the text
    engine.runAndWait() #process and play the queue


#main program execution function
if __name__ == '__main__':
    #initial greetings to the user (text and speech)
    print('Hello I am Jarvis AI your voice-commanded virtual assistant.')
    speechtx("Hello I am Jarvis AI your voice-commanded virtual assistant.")
    # main loop to keep the assistant running
    while True:
        command = sptext().lower() #get the command from sptext() function and convert into lowercase
        if 'jarvis' in command: #check for wake word
            print('I am ready for your command.') #status update
            speechtx("I am ready for your command.")
            while True: #command running loop
                    data1 = sptext().lower()
                    #list of sites
                    sites = [['youtube', 'https://www.youtube.com/'], ['chat gpt', 'https://chatgpt.com/'], ['github account', 'https://github.com/Jitenrai21']]
                    for site in sites: #loop to understand and open site as per the prompt
                        if f'Open {site[0]}'.lower() in data1: #understanding input
                            speechtx(f'Opening {site[0]}') #status update in audio
                            webbrowser.open(site[1]) #webbrowser package to open website
                    if "how are you" in data1: #looking for specific cue
                        reply = 'I am doing great, How are you?' #predefined output
                        print(reply) 
                        speechtx(reply)
                    if 'your name' in data1:
                        name = "It's so silly for you to ask again. My name is Javis."
                        print(name)
                        speechtx(name)
                    elif 'old are you' in data1:
                        age = "I have been created quite a while ago. By Jiten Rai, of course!"
                        print(age)
                        speechtx(age)
                    elif "time now" in data1:
                        time = datetime.datetime.now().strftime("%I%M%p") #%I gives hour, %M gives minute, %p gives am pm
                        print(f"The time is {time}")
                        speechtx(f"The time is {time}")
                    # elif 'youtube' in data1:
                    #     webbrowser.open('https://www.youtube.com/')
                    elif 'swift' in data1:
                        webbrowser.open('https://www.youtube.com/watch?v=X_e5z_XrlzY&list=PLe9t8KT-SdWXaS4thPTG66mazDoJ2-BJq&index=3')
                    elif 'joke' in data1:
                        joke = pyjokes.get_joke(language='en', category='all')
                        print(joke)
                        speechtx(joke)
                    # elif 'music' in data1:
                    #     add = r'C:\Users\ACER\OneDrive\Desktop\New folder'
                    #     list_of_song = os.listdir(add)
                    #     print(list_of_song)
                    #     os.startfile(os.path.join(add, list_of_song[0]))
                    elif 'open chrome' in data1:
                        speechtx('Opening google chrome.')
                        os.startfile(r'C:\Users\Public\Desktop\Google Chrome.lnk')
                    elif "exit" in data1:
                        print('I am always at your service. Come again.')
                        speechtx("I am always at your service. Come again.")
                        break    
                    # time.sleep(5)
            break
        else: #prompt user to use wake word if not detected
            print("Call by my name Jarvis for service.")
            speechtx("activate by calling me by my name Jarvis.")
            sptext() #continue listening for wake word
        