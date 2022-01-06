from src.core.task import Task 

class HelloWorldTask(Task):
    
    def __init__(self):
        super().__init__(["say hello world"])
        
    def action(self, text):
        
        return "Hello world"
        