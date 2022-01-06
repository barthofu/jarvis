import config
import os, sys, traceback
import pyaudio
import speech_recognition as sr
from pocketsphinx import DefaultConfig, Decoder, get_model_path, get_data_path

class STT:
    
    def __init__(self):
        
        # Create a decoder with certain model
        conf = DefaultConfig()
        conf.set_string('-hmm', os.path.join(get_model_path(), 'en-us'))
        conf.set_string('-dict', os.path.join(get_model_path(), 'cmudict-en-us.dict'))
        conf.set_string('-kws',   config.KEYPHRASES)

        self.decoder = Decoder(conf)
        self.p = pyaudio.PyAudio()
        
        self.r = sr.Recognizer()



    def waitForKeyword(self):
        with self._ignore_stderr():
            stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
            stream.start_stream()
            
            print("Waiting to be woken up...")
            # Process audio chunk by chunk. On keyword detected perform action and restart search
            self.decoder.start_utt()
            waiting = False
            waitCount = 0
            while True:
                buf = stream.read(1024, exception_on_overflow=False)
                self.decoder.process_raw(buf, False, False)
                if self.decoder.hyp():
                    if self.decoder.hyp().hypstr[:13] == "jarvis cancel" or self.decoder.hyp().hypstr[:11] == "jarvis stop":
                        self.decoder.end_utt()
                        return "jarvis stop"
                    else:
                        if waiting:
                            if waitCount >= 8:
                                self.decoder.end_utt()
                                return "jarvis"
                            else:
                                waitCount += 1
                        else:
                            waiting = True
        
        
        
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
