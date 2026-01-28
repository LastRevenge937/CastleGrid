import os
import time

class AURA_UI:
    def __init__(self, grid, sentinel, shadowgrid, config):
        self.grid = grid
        self.config = config

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def draw(self):
        self.clear()
        print(f"🏰 CASTLEGRID — {self.grid.castle_name}")
        print("=" * 40)
        for i in range(12):
            layer = self.grid.layers[i]
            print(f"[{i}] {layer.name:<15} | {layer.status}")
        print("\n[1] Cells  [2] Metrics  [3] GSG  [P] PURGE  [L] LASTREVENGE  [Q] Quit")

    def run(self):
        while True:
            self.draw()
            cmd = input("> ").strip().upper()

            if cmd == "Q":
                break
            elif cmd == "P":
                pw = input("Admin Password: ")
                if pw:
                    self.grid.activate_purge()
            elif cmd == "L":
                pw = input("Admin Password: ")
                if pw:
                    self.grid.activate_last_revenge()
