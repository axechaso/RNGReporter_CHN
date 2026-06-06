from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONFLICT_RE = re.compile(r"^(<<<<<<<|=======|>>>>>>>)", re.MULTILINE)
UI_STRING_RE = re.compile(
    r'\.(Text|HeaderText|ToolTipText|ToolTipTitle)\s*=\s*"(?P<value>(?:\\.|[^"\\])*)";'
)
ASCII_WORD_RE = re.compile(r"[A-Za-z]{4,}")
KEEP_WORDS = {
    "Ability",
    "Atk",
    "BID",
    "CID",
    "Cgear",
    "Delay",
    "Dream",
    "Frame",
    "GameCube",
    "Gear",
    "Hidden",
    "Method",
    "Nature",
    "None",
    "Power",
    "Seed",
    "Timer",
    "Timer0",
}


def scan_conflicts() -> list[str]:
    hits: list[str] = []
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".cs", ".resx", ".md", ".config"}:
            text = path.read_text(encoding="utf-8-sig", errors="ignore")
            if CONFLICT_RE.search(text):
                hits.append(str(path.relative_to(ROOT)))
    return hits


def scan_remaining_ui_english() -> list[tuple[str, str]]:
    hits: list[tuple[str, str]] = []
    for path in (ROOT / "RNGReporter").rglob("*.cs"):
        text = path.read_text(encoding="utf-8-sig", errors="ignore")
        for match in UI_STRING_RE.finditer(text):
            value = match.group("value")
            words = {word for word in ASCII_WORD_RE.findall(value) if word not in KEEP_WORDS}
            if words:
                hits.append((str(path.relative_to(ROOT)), value))
    return hits


def main() -> int:
    conflicts = scan_conflicts()
    english = scan_remaining_ui_english()
    if conflicts:
        print("Conflict markers:")
        for item in conflicts:
            print(f"  {item}")
    print(f"Remaining UI English candidates: {len(english)}")
    for path, value in english[:500]:
        print(f"{path}: {value}")
    return 1 if conflicts else 0


if __name__ == "__main__":
    raise SystemExit(main())
