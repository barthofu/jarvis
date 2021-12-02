import importlib
import pyaudio
import speech_recognition as sr
import config

from os import listdir, path
from utils import stt, tts

class Jarvis:
    
    def __init__(self):
        self.r = sr.Recognizer()
        self.stt = stt.STT()
        self.tts = tts.TTS()

        self.modules = type("", (), {})()
    
    
    
    def loadModules(self):
        
        files = listdir(path.abspath(__file__ + "/../../modules/"))
        
        for file in files:
            if (file.endswith('.py') and not file.startswith('_')):
                moduleName = file.split('.')[0]
                module = importlib.import_module(config.MODULES_IMPORT_DIR + '.' + moduleName)
                setattr(self.modules, moduleName, module)
    
    def matchModule (self, text):
        
        for module in list(self.modules.keys()):
            for task in module.tasks:
                pass
                
    
    def execModule(self, moduleName, actionName):
        module = getattr(self.modules, moduleName)
        action = getattr(module, actionName)()
        
        responseText = action.run()
        self.speak(responseText)
        
    
    def speak(self, text):
        if config.USE_TTS:
            tts.speak(text)
        else:
            print(text)
    
    
    def listen(self):
        while True:
            try:
                if config.USE_STT:
                    self.stt.waitForKeyword()
                    text = self.tts.activeListen()
                else:
                    text = input('> ')
                
                if not text:
                    print('No text input received.')
                    continue
                else:
                    print("'" + text + "'")
                    
                self.matchMods(text)
                self.executeMods(text)
                    
            except OSError as e:
                if 'Invalid input device' in str(e):
                    print('Invalid input device')
                    break
                else:
                    raise Exception
            except (EOFError, KeyboardInterrupt):
                print('Shutting down...')
                break
            except:
                print("(runtime error)")
