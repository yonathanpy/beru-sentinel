import json
import os

class Config:
    def __init__(self, path="config.json"):
        self.path = path
        self.data = self.load()

    def load(self):
        if not os.path.exists(self.path):
            return self.default()
        with open(self.path, "r") as f:
            return json.load(f)

    def default(self):
        return {
            "thread_limit": 50,
            "bruteforce_threshold": 40,
            "max_line_length": 1500
        }

    def get(self, key):
        return self.data.get(key)
