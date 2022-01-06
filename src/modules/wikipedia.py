from src.core.task import Task 

import wikipedia

class ExampleTask(Task):
    
    def __init__(self):
        super().__init__([
            "who is",
            "who the heck is"
        ], True)
        
    def action(self, text):
        
        personName = ' '.join(text.split()[-2:])
        return wikipedia.summary(personName)
        