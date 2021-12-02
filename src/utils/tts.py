import tempfile
import os
# import pygame
import config 
from playsound import playsound

from gtts import gTTS
# from pygame import mixer

class TTS:
    
    # def __init__(self):
    #     mixer.init()
        
        
        
    def playMP3(self, fileName, filePath = config.SOUNDS_DIR, blocking = False):
        """Plays a local MP3 file
        :param file_name: top-level file name (e.g. hello.mp3)
        :param file_path: directory containing file ('media' folder by default)
        :param blocking: if false, play mp3 in background
        """
        
        playsound(os.path.join(filePath, fileName))
        
        # if ".mp3" in fileName:
        #     mixer.music.load(os.path.join(filePath, fileName))
        #     mixer.music.play
        # else:
        #     sound = pygame.mixer.Sound(os.path.join(filePath, fileName))
        #     chan = pygame.mixer.find_channel()
        #     chan.queue(sound)

        # if blocking:
        #     while mixer.music.get_busy():
        #         pygame.time.delay(100)
          
          
                
    def speak(self, text, showText = True):
        """Speaks a given text phrase
        :param text: text string to speak
        :param showText: if True, print the text
        """
        
        if showText:
            print(text)

        try:
            tts = gTTS(text = text)

            with tempfile.NamedTemporaryFile(mode='wb', suffix='.mp3',
                                            delete=False) as f:
                (tempPath, tempName) = os.path.split(f.name)
                tts.write_to_fp(f)

            self.playMP3(tempName, tempPath)
            os.remove(os.path.join(tempPath, tempName))

        except Exception as e:
            print('Unknown Google TTS issue: ' + str(e))