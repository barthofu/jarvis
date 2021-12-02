import importlib
from os import listdir, path

class Brain:
    
    def __init__(self):
        self.modules = []
    
    def loadModules(self):
        
        files = listdir(path.abspath(__file__ + "/../../modules/"))
        
        for file in files:
            if (file.endswith('.py') and not file.startswith('_')):
                moduleName = file.split('.')[0]
                module = importlib.import_module('src.modules.' + moduleName)
                
                tasks = []
                print()
                for taskKey in [*dict([(name, cls) for name, cls in module.__dict__.items() if isinstance(cls, type)])]:
                    task = getattr(module, taskKey)
                    instanciedTask = task(['musique'])
                    tasks.append(instanciedTask)
                    
                self.modules.append({
                    'name': moduleName,
                    'tasks': tasks   
                })

                
                
        
    def execModule(self, moduleName, className):
        module = getattr(self.modules, moduleName)
        classAction = getattr(module, className)()
        
        classAction.run() 
        
    def matchModule (self, text):
        
        for module in self.modules:
            for task in module['tasks']:
                print(task)
                print(task.match(text))