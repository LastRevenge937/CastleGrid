class ShadowGrid:
    def __init__(self, grid):
        self.grid = grid
        self.captured_files = []

    def capture_from_honeypot(self, grid_file):
        grid_file.freeze("Captured by Honeypot → ShadowGrid")
        self.captured_files.append(grid_file)
        self.grid.log_global(f"ShadowGrid captured {grid_file.name}")

