from src.utils.task import Task 

from sense_hat import SenseHat

class CurrentTemparatureTask(Task):
    
    def __init__(self):
        super().__init__([
            'what is temperature',
            'current temperature'
        ])

        self.sense = SenseHat()
        
    def action(self, text):
        
        temp = self.sense.get_temperature()
        return f"Currently, it is {temp} degrees"