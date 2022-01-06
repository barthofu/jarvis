import speech_recognition as sr
import pocketsphinx

keywords = [
    ("hey jarvis", 1)
]

def speech2text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source) #this is were i want to listen in the background to run it at the same 
        #time as other code
    try:
        data = r.recognize_sphinx(audio, keyword_entries = keywords)
        return data
    except:
        return "Error..."

while True:
    print(speech2text())