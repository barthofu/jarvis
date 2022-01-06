import importlib
import pyaudio
import speech_recognition as sr
import config

from os import listdir, path
from utils import stt, tts, parser

class Jarvis:
    
    def __init__(self):
        self.r = sr.Recognizer()
        self.stt = stt.STT()
        self.tts = tts.TTS()

        self.modules = []
    
    
    def loadModules(self):
        
        files = listdir(path.abspath(__file__ + "/../../modules/"))
        
        for file in files:
            if (file.endswith('.py') and not file.startswith('_')):
                moduleName = file.split('.')[0]
                module = importlib.import_module(config.MODULES_IMPORT_DIR + '.' + moduleName)
                
                tasks = []
                for taskKey in [*dict([(name, cls) for name, cls in module.__dict__.items() if isinstance(cls, type)])]:
                    if taskKey.endswith('Task') and taskKey != 'Task':
                        Task = getattr(module, taskKey)
                        instanciedTask = Task()
                        tasks.append(instanciedTask)
                    
                self.modules.append({
                    'name': moduleName,
                    'tasks': tasks   
                })
    

    def matchTask (self, text):

        matches = []

        for module in self.modules:
            for task in module['tasks']:

                ratio = max(task.match(text))

                # if the ratio is suffisent enough and the task has a stop priority option, it will directly return it
                if ratio > config.TRESHOLD and task.stopPriority:
                    return task
                
                matches.append({
                    'task': task,
                    # we search for the highest ratio among all the phrases triggers of the task
                    'ratio': ratio
                })

        # sort by ratio in descending order to find the max one
        matches = sorted(matches, key = lambda x: x['ratio'], reverse = True)

        return matches[0]['task']
                
    
    def executeTask(self, task, text):
        
        responseText = task.action(text)
        self.speak(responseText)
        
    
    def speak(self, text):

        if config.USE_TTS:
            self.tts.speak(text)
        else:
            print(text)
    
    
    def listen(self):


        if config.USE_STT:
            # self.stt.waitForKeyword()
            text = self.tts.activeListen()
            if not text:
                print('No text input received.')
                return
            else:
                print("'" + text + "'")
        else:
            text = input('> ')

        text = parser.parse(text)
            
        task = self.matchTask(text)
        self.executeTask(task, text)
            
