import threading
from collections import defaultdict

class Storage:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = defaultdict(list)

    def add(self, key, value):
        with self.lock:
            self.data[key].append(value)

    def all(self):
        return dict(self.data)
