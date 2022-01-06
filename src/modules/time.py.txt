from src.utils.task import Task 

from datetime import datetime
from sense_hat import SenseHat
import time

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
    
    

class DisplayHourTask(Task):

    def __init__(self):
        super().__init__([
            'display hour'
        ])

        self.sense = SenseHat()
        self.numbers = [
            [[0,1,1,1], # Zero
            [0,1,0,1],
            [0,1,0,1],
            [0,1,1,1]],
            [[0,0,1,0], # One
            [0,1,1,0],
            [0,0,1,0],
            [0,1,1,1]],
            [[0,1,1,1], # Two
            [0,0,1,1],
            [0,1,1,0],
            [0,1,1,1]],
            [[0,1,1,1], # Three
            [0,0,1,1],
            [0,0,1,1],
            [0,1,1,1]],
            [[0,1,0,1], # Four
            [0,1,1,1],
            [0,0,0,1],
            [0,0,0,1]],
            [[0,1,1,1], # Five
            [0,1,1,0],
            [0,0,1,1],
            [0,1,1,1]],
            [[0,1,0,0], # Six
            [0,1,1,1],
            [0,1,0,1],
            [0,1,1,1]],
            [[0,1,1,1], # Seven
            [0,0,0,1],
            [0,0,1,0],
            [0,1,0,0]],
            [[0,1,1,1], # Eight
            [0,1,1,1],
            [0,1,1,1],
            [0,1,1,1]],
            [[0,1,1,1], # Nine
            [0,1,0,1],
            [0,1,1,1],
            [0,0,0,1]]
        ]

        self.noNumber = [0, 0, 0, 0]

        self.hourColor = [255,0,0] # Red
        self.minuteColor = [0,255,255] # Cyan
        self.empty = [0,0,0] # Black/Off


    def action(self, text):

        clockImage = []
        hour = time.localtime().tm_hour
        minute = time.localtime().tm_min

        for index in range(0, 4):
            if (hour >= 10):
                clockImage.extend(self.numbers[int(hour/10)][index])
            else:
                clockImage.extend(self.noNumber)
            clockImage.extend(self.numbers[int(hour%10)][index])
            
        for index in range(0, 4):
            clockImage.extend(self.numbers[int(minute/10)][index])
            clockImage.extend(self.numbers[int(minute%10)][index])
            
        for index in range(0, 64):
            if (clockImage[index]):
                if index < 32:
                    clockImage[index] = self.hourColor
                else:
                    clockImage[index] = self.minuteColor
            else:
                clockImage[index] = self.empty
                
        self.sense.set_rotation(90) # Optional
        self.sense.low_light = True # Optional
        self.sense.set_pixels(clockImage)

        