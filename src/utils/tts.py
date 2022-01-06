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