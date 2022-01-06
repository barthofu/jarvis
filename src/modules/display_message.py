from src.utils.task import Task 

from sense_hat import SenseHat

class DisplayMessageTask(Task):
    
    def __init__(self):
        super().__init__([
            'display the message'
        ])

        self.sense = SenseHat()
        
    def action(self, text):

        message = ' '.join(text.split('message'))
        
        self.sense.show_message(message)
        
        return ''
        