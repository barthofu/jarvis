from src.core.task import Task 

from picamera import PiCamera
from time import sleep

class CameraTask(Task):
    
    def __init__(self):
        super().__init__([
            "record"
        ])
        self.camera = PiCamera()
        self.defaultRecordTime = 10
        
    def action(self, text):
        
        self.camera.start_preview()
        sleep(self.defaultRecordTime)
        self.camera.stop_preview()

        return ""
        