from core.gfid import GFID

class GridFile:
    def __init__(self, name: str):
        self.name = name
        self.gfid = GFID()
        self.read_only = False

        self.gfid.log(f"File created: {name}")

    def freeze(self, reason: str):
        self.read_only = True
        self.gfid.log(f"File frozen: {reason}")
