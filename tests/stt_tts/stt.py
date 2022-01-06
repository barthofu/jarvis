import pyaudio,os
import speech_recognition as sr
r = sr.Recognizer()

KEYWORD = 'tomato'

def excel():
        os.system("start excel.exe")

def internet():
        os.system("start chrome.exe")

def media():
        os.system("start wmplayer.exe")

def activeListening():
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)

def passiveListening():
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
        if text == KEYWORD:
            return True
        else:
            return False

while 1:
    if (passiveListening()):
        print('start listening')
        activeListening()



# import pyaudio
# import speech_recognition as sr
# r = sr.Recognizer()
# with sr.Microphone() as source : 
#     print("say something")
#     audio = r.listen(source)
    
# try : 
#     print(r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("not understand")
# except sr.RequestError as e :
#     print(e)