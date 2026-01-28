import time
from core.identity import CastleIdentity

identity = CastleIdentity()
identity.load()

def post(self, message: str):
    entry = f"[{identity.name}] {message}"
    self._append(entry)

class NewsFeed:
    def __init__(self):
        self.entries = []

    def post(self, message: str):
        self.entries.append((time.ctime(), message))

    def latest(self, limit=5):
        return self.entries[-limit:]
