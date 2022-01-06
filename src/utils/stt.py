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
                # r.adjust_for_ambient_noise(src)
                print("Active listening... ")
                #tts.playMP3('double-beep.wav')

                # listen for the first phrase and extract it into audio data
                audio = self.r.listen(source)

        text = ''
        try:
            if config.ACTIVE_ENGINE == "google":
                text = self.r.recognize_google(audio)  # recognize speech using Google STT
            elif config.ACTIVE_ENGINE == "sphinx":
                text = self.r.recognize_sphinx(audio)
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError as e:
            print("Could not request results from Google STT; {0}".format(e))
        except:
            print("Unknown exception occurred!")
            print(traceback.format_exc())
        finally:
            return text
        
        
        
    def _ignore_stderr(self):
        """ Ignore unwanted 'error' output from pyglet/pyaudio """
        devnull = os.open(os.devnull, os.O_WRONLY)
        old_stderr = os.dup(2)
        sys.stderr.flush()
        os.dup2(devnull, 2)
        os.close(devnull)
        try:
            yield
        finally:
            os.dup2(old_stderr, 2)
            os.close(old_stderr)
