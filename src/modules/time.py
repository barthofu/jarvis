from src.core.task import Task 

from datetime import datetime

class HourTask(Task):
    
    def __init__(self):
        super().__init__([
            'what is hour',
            'what is time'
        ])
        
    def action(self, text):
        now = datetime.now()
        return f"It is {now.strftime('%I')} {now.strftime('%M')} {now.strftime('%p')}"
    


class DayTask(Task):
    
    def __init__(self):
        super().__init__([
            'what is date',
            'what is day'
        ])
        
    def action(self, text):
        now = datetime.now()
        return f"We are the {now.strftime('%d')} {now.strftime('%B')}"
    
    
        