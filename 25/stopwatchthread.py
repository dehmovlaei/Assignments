import time
from PySide6.QtCore import *
from mytime import MyTime


class StopWatchThread(QThread):
    signal_counter = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 0, 0)

    def run(self):
        while True:
            self.time.plus()
            self.signal_counter.emit(self.time)
            time.sleep(1)

    def reset(self):
        self.time.second = 0
        self.time.minutes = 0
        self.time.hour = 0