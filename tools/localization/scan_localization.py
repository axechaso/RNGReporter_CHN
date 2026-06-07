from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONFLICT_RE = re.compile(r"^(<<<<<<<|=======|>>>>>>>)", re.MULTILINE)
UI_STRING_RE = re.compile(
    r'\.(Text|HeaderText|ToolTipText|ToolTipTitle|Filter|Title)\s*=\s*"(?P<value>(?:\\.|[^"\\])*)";'
)
MESSAGE_BOX_RE = re.compile(r"MessageBox\.Show\s*\((?P<body>.*?)\);", re.DOTALL)
STRING_RE = re.compile(r'(?<![@\w])"(?P<value>(?:\\.|[^"\\])*)"')
ASCII_WORD_RE = re.compile(r"[A-Za-z]{4,}")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")
IGNORE_UI_VALUES = {
    "Deutsch",
    "English",
    "Español",
    "Français",
    "Italiano",
    "Tick 2: ",
    "Tick: ",
}
KEEP_WORDS = {
    "Ability",
    "Atk",
    "BID",
    "CID",
    "Cgear",
    "Deutsch",
    "Delay",
    "DPPt",
    "Dream",
    "English",
    "Español",
    "Frame",
    "Français",
    "GameCube",
    "Gear",
    "GxStat",
    "HBit",
    "HGSS",
    "Hidden",
    "Italiano",
    "LBit",
    "Method",
    "Nature",
    "None",
    "PRNG",
    "Power",
    "RunAsDate",
    "Seed",
    "Timer",
    "Timer0",
    "Tick",
    "VCount",
    "VFrame",
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
            if value in IGNORE_UI_VALUES:
                continue
            if CJK_RE.search(value):
                continue
            words = {word for word in ASCII_WORD_RE.findall(value) if word not in KEEP_WORDS}
            if words:
                hits.append((str(path.relative_to(ROOT)), value))
    return hits


def scan_remaining_messagebox_english() -> list[tuple[str, str]]:
    hits: list[tuple[str, str]] = []
    for path in (ROOT / "RNGReporter").rglob("*.cs"):
        text = path.read_text(encoding="utf-8-sig", errors="ignore")
        for call in MESSAGE_BOX_RE.finditer(text):
            for match in STRING_RE.finditer(call.group("body")):
                value = match.group("value")
                if value.startswith(("http://", "https://")):
                    continue
                if CJK_RE.search(value):
                    continue
                words = {word for word in ASCII_WORD_RE.findall(value) if word not in KEEP_WORDS}
                if words:
                    hits.append((str(path.relative_to(ROOT)), value))
    return hits


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    conflicts = scan_conflicts()
    english = scan_remaining_ui_english()
    messagebox = scan_remaining_messagebox_english()
    if conflicts:
        print("Conflict markers:")
        for item in conflicts:
            print(f"  {item}")
    print(f"Remaining UI English candidates: {len(english)}")
    for path, value in english[:500]:
        print(f"{path}: {value}")
    print(f"Remaining MessageBox English candidates: {len(messagebox)}")
    for path, value in messagebox[:500]:
        print(f"{path}: {value}")
    return 1 if conflicts or english or messagebox else 0


if __name__ == "__main__":
    raise SystemExit(main())
