from src.utils.task import Task 

class ExampleTask(Task):
    
    def __init__(self):
        super().__init__([])
        
    def action(self, text):
        
        return "1"
        