from pathlib import Path
import json
import uuid

IDENTITY_FILE = Path("data/castle_identity.json")

class CastleIdentity:
    def __init__(self):
        self.name = None
        self.uuid = None

    def load(self) -> bool:
        if IDENTITY_FILE.exists():
            with open(IDENTITY_FILE, "r") as f:
                data = json.load(f)
                self.name = data["name"]
                self.uuid = data["uuid"]
            return True
        return False

    def initialize(self, name: str):
        self.name = name
        self.uuid = str(uuid.uuid4())
        IDENTITY_FILE.parent.mkdir(exist_ok=True)
        with open(IDENTITY_FILE, "w") as f:
            json.dump(
                {"name": self.name, "uuid": self.uuid},
                f,
                indent=2
            )
