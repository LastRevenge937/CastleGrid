class Layer:
    def __init__(self, index: int, name: str):
        self.index = index
        self.name = name
        self.cells = []
        self.status = "Offline"

    def add_cell(self, cell):
        self.cells.append(cell)

    def boot(self):
        self.status = "Online"
        for c in self.cells:
            c.start()

    def shutdown(self):
        self.status = "Locked"
        for c in self.cells:
            c.shutdown()
