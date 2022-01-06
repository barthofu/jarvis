import pywhatkit
import datetime
import pyjokes
import wikipedia
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math


command = 'play mardis gras'
if 'play' in command:
    song = command.replace('play', '')
    pywhatkit.playonyt(song)
elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        
        

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

currentVolumeDb = volume.GetMasterVolumeLevel()
volume.SetMasterVolumeLevel(currentVolumeDb - 6.0, None)
