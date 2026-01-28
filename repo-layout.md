# Architectural Layout of the Grid included in this repo

castlegrid/
│
├── main.py                     # Entry point / bootstrap
├── cli/
│   └── ascii_ui.py             # ASCII numeric UI
│
├── core/
│   ├── grid.py                 # CastleGrid manager
│   ├── layer.py                # Layer abstraction
│   ├── cell.py                 # Base Cell class
│   ├── gfid.py                 # GFID + immutable ledger
│   ├── file.py                 # GridFile object
│
├── ai/
│   ├── sentinel.py             # Sentinel AI (global authority)
│   ├── shadowgrid.py           # ShadowGrid controller
│   ├── doctrine.py             # Doctrine schema + approval
│
├── layers/
│   ├── limbo.py
│   ├── courtyard.py
│   ├── infrastructure.py
│   ├── operations.py
│   ├── secured_transit.py
│   ├── pier.py
│   ├── quarantine.py
│   ├── arena.py                # PURGATORY
│   ├── crown_vaults.py
│   ├── rinzler_factory.py
│   ├── private_shadowgrid.py
│   └── deadman_core.py
│
├── analyzers/
│   └── static_python.py        # Safe static analysis only
│
└── logs/
    └── arena.log               # Append‑only
