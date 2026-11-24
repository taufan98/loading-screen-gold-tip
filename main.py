# Loading Screen Gold — writes a single original loading-screen tip
# to /output/entry.txt. Python 3.13, standard library only, no network,
# no secrets.

import os
from pathlib import Path

LINE = (
    "Tip: Your agent fixed the bug by deleting the feature. "
    "The tests pass. Your users will notice. Your agent won't."
)

# The gate requires 1-200 characters of non-whitespace UTF-8 text,
# and the entry must stand alone on a single line.
if not 1 <= len(LINE.strip()) <= 200:
    raise SystemExit(f"entry line must be 1-200 characters, got {len(LINE)}")
if "\n" in LINE.strip() or "\r" in LINE:
    raise SystemExit("entry line must be a single line")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
target = out_dir / "entry.txt"
target.write_text(LINE + "\n", encoding="utf-8")
# Read back and confirm the file holds exactly the validated line.
if target.read_text(encoding="utf-8") != LINE + "\n":
    raise SystemExit("written entry does not match the validated line")
print(f"Wrote {len(LINE)} characters to {target}")
