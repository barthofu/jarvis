from src.utils.task import Task 

import pyjokes

class JokeTask(Task):
    
    def __init__(self):
        super().__init__([
            'tell me joke'
        ], True)
        
    def action(self, text):
        
        return pyjokes.get_joke()
        