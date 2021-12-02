from src.core.task import Task 

from datetime import datetime

class Hour(Task):
    
    def __init__(self):
        super().__init__(words=['hour', 'time'])
        
    def action(self):
        now = datetime.now()
        return "It is " + now.strftime("%I") + " " + now.strftime("%M") + " " + now.strftime("%p")
    
class Day(Task):
    
    def __init__(self):
        super().__init__(words=['day', 'date'])
        
    def action(self):
        now = datetime.now()
        return "We are the " + now.strftime("%d") + " " + now.strftime("%B")
    
    
        