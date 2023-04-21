
from pathlib import Path
import os

ROOT = Path("/home/minecraft")
TOOL = ROOT / "tools"
PAPER_1_19_3 = ROOT / "paper1.19.3"

os.execv(PAPER_1_19_3 / "mgmt.sh", ["1", "6"])

