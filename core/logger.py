import threading
from datetime import datetime

class Logger:
    def __init__(self):
        self.lock = threading.Lock()

    def log(self, level, msg):
        with self.lock:
            print(f"[{datetime.now()}] [{level}] {msg}")

logger = Logger()
