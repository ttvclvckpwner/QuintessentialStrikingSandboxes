import pyttsx3
import webbrowser
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys
from gtts import gTTS

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voice')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait

  speak("I am JARVIS Sir. Please tell me how I may help you")

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your digital assistant JARVIS!')
speak('How may I help you?')

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        webbrowser = r.recognize_google(audio, language='en-in')
        print('User: ' + webbrowser + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        webbrowser = str(input('Command: '))

    return
    webbrowser
    myCommand()
        
if __name__ == '__main__':

  while True:
      if 'open youtube' in  webbrowser:
            speak('okay')
            webbrowser.open('www.youtube.com')

      elif 'open google' in webbrowser:
            speak('okay')
            webbrowser.open('www.google.co.in')
        
      elif 'nothing' in webbrowser or 'abort' in webbrowser or 'stop' in webbrowser:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
      elif 'hello' in webbrowser:
            speak('Hello Sir')

      elif ('bye') in webbrowser:
          speak('ok sir')
          speak('closing all systems')
          speak('disconnecting to servers')
          speak('going offline')
          quit()