import tempfile, os
import config 
from playsound import playsound

from gtts import gTTS

class TTS:
        
    def playMP3(self, fileName, filePath = config.SOUNDS_DIR, blocking = False):

        playsound(os.path.join(filePath, fileName))

                
    def speak(self, text, showText = True):
        
        if showText:
            print(text)

        try:
            # we first create a temp mp3 file of the audio output
            tts = gTTS(text = text)
            with tempfile.NamedTemporaryFile(mode='wb', suffix='.mp3', delete=False) as f:
                (tempPath, tempName) = os.path.split(f.name)
                tts.write_to_fp(f)

            # and then we play it
            self.playMP3(tempName, tempPath)
            
            os.remove(os.path.join(tempPath, tempName))

        except Exception as e:
            print('Unknown Google TTS issue: ' + str(e))