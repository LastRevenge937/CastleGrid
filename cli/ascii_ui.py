import os
from core.security import verify_password
from metrics.system_metrics import SystemMetrics


class AURA_UI:
    """
    Main ASCII UI for CastleGrid
    """

    def __init__(self, grid, sentinel, shadowgrid, config):
        self.grid = grid
        self.sentinel = sentinel
        self.shadowgrid = shadowgrid
        self.config = config

    # -------------------------
    # Helpers
    # -------------------------
    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    # -------------------------
    # Main Draw
    # -------------------------
    def draw(self):
        self.clear()
        print(f"🏰 CASTLEGRID — {self.grid.castle_name}")
        print(f"Protocol: {self.grid.protocol}\n")

        print("┌──────────────────────── CASTLEGRID ────────────────────────┐")
        for i in range(12):
            layer = self.grid.layers[i]
            print(
                f"│ [{i:<2}] {layer.name:<20} │ {layer.description:<28} │ {layer.status:<6} │"
            )
        print("└────────────────────────────────────────────────────────────┘\n")

        print("[1] Cells   [2] Metrics   [3] GSG / ShadowGrid")
        print("[4] Security (Firewalls / PURGATORY / Doctrines)")
        print("[P] PURGE   [L] LAST_REVENGE   [Q] Quit\n")

    # -------------------------
    # Main Loop
    # -------------------------
    def run(self):
        while True:
            self.draw()
            cmd = input("> ").strip().upper()

            if cmd == "Q":
                break

            elif cmd in ("P", "L"):
                pw = input("Admin Password: ")
                if not verify_password(pw, self.config["hash"]):
                    input("Invalid password. Press Enter...")
                    continue

                if cmd == "P":
                    self.grid.activate_purge()
                else:
                    self.grid.activate_last_revenge()

            elif cmd == "1":
                self.show_cells()

            elif cmd == "2":
                self.show_metrics()

            elif cmd == "3":
                self.show_gsg()

            elif cmd == "4":
                self.show_security()

            else:
                input("Unknown command. Press Enter...")

    # -------------------------
    # Cells View
    # -------------------------
    def show_cells(self):
        self.clear()
        print("=== CELL STATUS ===\n")
        for layer in self.grid.layers.values():
            print(f"Layer {layer.index}: {layer.name}")
            for cell in layer.cells:
                print(f"  - {cell.name}")
            print()
        input("Press Enter to return...")

    # -------------------------
    # Metrics View
    # -------------------------
    def show_metrics(self):
        self.clear()
        metrics = SystemMetrics().snapshot()
        print("=== SYSTEM METRICS ===\n")
        for k, v in metrics.items():
            print(f"{k}: {v}")
        input("\nPress Enter to return...")

    # -------------------------
    # GSG / ShadowGrid View (MERGED)
    # -------------------------
    def show_gsg(self):
        self.clear()
        print("=== GLOBAL SHADOW GRID ===\n")

        print(f"Captured Files: {len(self.shadowgrid.captured_files)}")
        print("Recent GSG News:\n")

        if hasattr(self.shadowgrid.gsg, "news"):
            for entry in self.shadowgrid.gsg.news.latest():
                print(f"[{entry['timestamp']}] {entry['message']}")
        else:
            print("No news available.")

        input("\nPress Enter to return...")

    # -------------------------
    # Security View (NEW)
    # -------------------------
    def show_security(self):
        self.clear()
        print("=== SECURITY OVERVIEW ===\n")

        print("Active Firewalls:")
        fw_report = self.sentinel.firewall_status_report()
        if fw_report:
            for line in fw_report:
                print(f" - {line}")
        else:
            print(" - None")

        print("\nPURGATORY Runs:")
        runs = getattr(self.shadowgrid, "purgatory_runs", [])
        if runs:
            for r in runs[-5:]:
                print(f" - {r}")
        else:
            print(" - No runs recorded")

        print("\nDoctrine Status:")
        if hasattr(self.shadowgrid, "doctrines"):
            for state in ["pending", "approved", "rejected", "needs_testing"]:
                count = len(list((self.shadowgrid.doctrines.root / state).glob("*.json")))
                print(f" - {state}: {count}")
        else:
            print(" - Doctrine system offline")

        input("\nPress Enter to return...")



