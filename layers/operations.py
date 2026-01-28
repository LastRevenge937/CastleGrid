from core.layer import Layer
from core.cell import Cell

def build_operations():
    layer = Layer(3, "OPERATIONS")

    cells = [
        "Workflow Cell",
        "Batch Transfer Cell",
        "Update Staging Cell",
        "Process Organizer",
        "Agent Coordination"
    ]

    for c in cells:
        layer.add_cell(Cell(c))

    return layer
