import pyaudio
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source : 
    print("say something")
    audio = r.listen(source)
    
try : 
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("not understand")
except sr.RequestError as e :
    print(e)



# from difflib import SequenceMatcher

# treshold = 0.6

# removableSubstrings = [ 'hey jarvis', ',', 'please', 'the', ' a ', 'an' ]
# requiredStr = "turn on light"

# def processString (str):
#     for item in removableSubstrings:
#         str = str.replace(item, '')
#     return str.replace('  ', ' ').replace('  ', ' ').strip()

# str = "hey jarvis, what time is it"

# print(processString(str))

# seq = SequenceMatcher(None, requiredStr, processString(str))
# print(seq.ratio())
# print((seq.ratio() > treshold))