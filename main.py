import os
import json
import hashlib
from core.grid import GridManager
from ai.sentinel import Sentinel
from ai.shadowgrid import ShadowGrid
from cli.ascii_ui import AURA_UI
from gsg.gsg_core import GlobalShadowGrid

def main():
    cfg = load_config()
    grid = GridManager(cfg["castle"])
    sentinel = Sentinel(grid)
    gsg = GlobalShadowGrid()
    shadowgrid = ShadowGrid(grid, gsg)

    grid.generate_all_layers()
    grid.boot_layers()

    # First boot messages
    print(f"Welcome to {cfg['castle']}. Sentinel and ShadowGrid are online.")
    print(f"GSG connected: {len(gsg.captured_files)} captured files.")

    ui = AURA_UI(grid, sentinel, shadowgrid, cfg)
    ui.run()

CONFIG = "config/castle_config.json"

def first_boot():
    os.makedirs("config", exist_ok=True)
    print("🏰 Welcome to CastleGrid")
    name = input("Name your Castle: ")
    password = input("Set Admin Password: ")

    data = {
        "castle": name,
        "hash": hashlib.sha256(password.encode()).hexdigest()
    }

    with open(CONFIG, "w") as f:
        json.dump(data, f)

    return data

def load_config():
    if not os.path.exists(CONFIG):
        return first_boot()
    with open(CONFIG) as f:
        return json.load(f)

def main():
    cfg = load_config()
    grid = GridManager(cfg["castle"])
    sentinel = Sentinel(grid)
    shadowgrid = ShadowGrid(grid)

    grid.generate_all_layers()
    grid.boot_layers()

    ui = AURA_UI(grid, sentinel, shadowgrid, cfg)
    ui.run()

if __name__ == "__main__":
    main()



