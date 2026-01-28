import time

class NewsFeed:
    def __init__(self):
        self.entries = []

    def post(self, message: str):
        self.entries.append((time.ctime(), message))

    def latest(self, limit=5):
        return self.entries[-limit:]
