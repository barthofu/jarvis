from src.utils.task import Task 

from sense_hat import SenseHat

class LightsOnTask(Task):
    
    def __init__(self):
        super().__init__([
            'turn on lights',
            'switch on lights'
        ])

        self.sense = SenseHat()
        
    def action(self, text):
        
        self.sense.clear(255, 255, 255)
        return 'Okay, I turn on the lights'



class LightsOffTask(Task):
    
    def __init__(self):
        super().__init__([
            'turn off lights',
            'switch off lights'
        ])

        self.sense = SenseHat()
        
    def action(self, text):
        
        self.sense.clear()
        return 'Okay, I turn off the lights'
        