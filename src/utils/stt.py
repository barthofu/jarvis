import config
import os, sys, traceback
import pyaudio
import speech_recognition as sr

class STT:
    
    def __init__(self):
        
        self.p = pyaudio.PyAudio()
        self.r = sr.Recognizer()
        
        
    def activeListen(self):

        with self._ignore_stderr():
            with sr.Microphone() as source:
                # listen for 1 second to adjust energy threshold for ambient noise
                self.r.adjust_for_ambient_noise(source)

                # notify that jarvis is listening
                print("Active listening... ")

                # listen for the first phrase and extract it into audio data
                audio = self.r.listen(source)

        # recognize speech using Google STT API
        text = self.r.recognize_google(audio)

        return text





        