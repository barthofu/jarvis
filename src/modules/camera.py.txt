from src.utils.task import Task 

from picamera import PiCamera
from time import sleep

class CameraTask(Task):
    
    def __init__(self):
        super().__init__([
            "start recording",
            "record"
        ])
        self.camera = PiCamera()
        self.defaultRecordTime = 10
        
    def action(self, text):
        
        self.camera.start_preview()
        sleep(self.defaultRecordTime)
        self.camera.stop_preview()

        return ""
        