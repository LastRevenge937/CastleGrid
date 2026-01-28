from core.layer import Layer
from core.cell import Cell

def build_infrastructure():
    layer = Layer(2, "INFRASTRUCTURE")

    cells = [
        "CPU Monitor",
        "GPU Monitor",
        "RAM Monitor",
        "Storage Tracker",
        "Resource Balancer",
        "Scheduler",
        "Telemetry"
    ]

    for c in cells:
        layer.add_cell(Cell(c))

    return layer
