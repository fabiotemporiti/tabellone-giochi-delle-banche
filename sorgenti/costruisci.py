# Copyright 2026 Fabio Temporiti
# SPDX-License-Identifier: EUPL-1.2
"""Genera il tabellone (un unico file HTML offline) inserendo i dati delle carte nel modello."""
import json
from pathlib import Path

qui = Path(__file__).parent
modello = (qui / "modello.html").read_text(encoding="utf-8")
dati = json.loads((qui / "dati.json").read_text(encoding="utf-8"))
assert modello.count("__DATI__") == 1
uscita = qui.parent / "i-Giochi-delle-Banche-tabellone-persona-facilitatrice.html"
uscita.write_text(modello.replace("__DATI__", json.dumps(dati, ensure_ascii=False)), encoding="utf-8")
print("scritto", uscita.name)
