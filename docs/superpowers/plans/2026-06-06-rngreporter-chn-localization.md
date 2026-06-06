# RNGReporter Chinese Localization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port the existing CHN localization onto Bambo-Rambo RNGReporter, translate new target-only UI text, and generate a review file for user校对.

**Architecture:** Keep Bambo-Rambo `master` as the canonical codebase and use `axechaso/RNGReporter_CHN` only as a translation source. Use small Python utilities to apply safe mechanical transfers, then manually review target-only forms and uncertain strings. Preserve upstream behavior by copying CHN files only when Bambo did not modify that file after the common ancestor.

**Tech Stack:** Windows PowerShell, Git, Python 3, C# WinForms, `.resx` XML resources, .NET Framework 4.8 target project.

---

## File Structure

- Create `tools/localization/migrate_chinese_localization.py`
  - Computes the common ancestor, changed-file sets, safe CHN-only file copies, `.resx` key merges, WinForms property transfer, and review entries.
- Create `tools/localization/scan_localization.py`
  - Reports conflict markers, remaining English UI strings, and generated review rows.
- Create `translation-review.md`
  - User-facing校对 list with source path, original English, proposed Chinese, and status.
- Modify many existing `RNGReporter/**/*.cs`, `RNGReporter/**/*.Designer.cs`, and `RNGReporter/**/*.resx`
  - Apply migrated or new Chinese UI text.
- Keep `C:\Users\axenx\Documents\rngreporter` read-only
  - It remains the CHN reference checkout.

## Task 1: Confirm Baseline And Branch

**Files:**
- Modify: repository metadata only

- [ ] **Step 1: Confirm target repository and clean status**

Run:

```powershell
git status --short --branch
git remote -v
git rev-parse --show-toplevel
```

Expected:

```text
## master...origin/master [ahead 1]
origin  https://github.com/Bambo-Rambo/RNGReporter.git (fetch)
origin  https://github.com/Bambo-Rambo/RNGReporter.git (push)
C:/Users/axenx/AppData/Local/Temp/codex-rngreporter-bambo
```

- [ ] **Step 2: Create a working branch**

Run:

```powershell
git switch -c codex/chn-localization
```

Expected: branch switches to `codex/chn-localization`.

- [ ] **Step 3: Confirm CHN remote exists**

Run:

```powershell
git remote -v
git fetch chn master
git merge-base master chn/master
```

Expected: `chn` remote points to `https://github.com/axechaso/RNGReporter_CHN.git`, fetch succeeds, merge-base is `2c77b8eeed2a725b1b924ff3dfde2ab84e684491`.

## Task 2: Add Localization Migration Utility

**Files:**
- Create: `tools/localization/migrate_chinese_localization.py`
- Create: `tools/localization/scan_localization.py`
- Modify: `translation-review.md` after running scripts

- [ ] **Step 1: Create migration script**

Create `tools/localization/migrate_chinese_localization.py` with these responsibilities:

```python
from __future__ import annotations

import csv
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
REVIEW_PATH = ROOT / "translation-review.md"
BASE_REF = "2c77b8eeed2a725b1b924ff3dfde2ab84e684491"
CHN_REF = "chn/master"
TRANSLATABLE_SUFFIXES = {".cs", ".resx", ".md", ".config"}
COPY_SUFFIXES = {".cs", ".resx"}

TEXT_PROPERTIES = {
    "Text",
    "HeaderText",
    "ToolTipText",
    "ToolTipTitle",
    "Filter",
}

MANUAL_TRANSLATIONS = {
    "Gen 5 FrameFinder": "第五世代帧查找器",
    "Gen 5 Frame Finder": "第五世代帧查找器",
    "Chatot Pitches": "聒噪鸟音高",
    "Any": "任意",
    "Low": "低",
    "Mid-Low": "中低",
    "Mid": "中",
    "Mid-High": "中高",
    "High": "高",
    "Mid-Low / Low": "中低 / 低",
    "Mid / Mid-Low": "中 / 中低",
    "Mid-High / Mid": "中高 / 中",
    "High / Mid-High": "高 / 中高",
    "Jump to selected frame": "跳转到所选帧",
    "Possible Results:": "可能结果:",
    "Clear": "清除",
    "Remove": "移除",
    "C-Gear Calibrator": "C-Gear 校准器",
    "Target Seed": "目标 Seed",
    "Target Delay": "目标 Delay",
    "IV Frame": "IV 帧",
    "RNG Info": "RNG 信息",
    "Wild IVs": "野生 IV",
    "Difference": "差值",
    "New Delay": "新 Delay",
    "Pickup": "拾取",
    "Target Item": "目标道具",
    "Notes:": "备注:",
    "Active Roamer": "活动游走宝可梦",
    "Party 1": "队伍 1",
    "Party 2": "队伍 2",
    "Party 3": "队伍 3",
    "Party 4": "队伍 4",
    "Party 5": "队伍 5",
    "Party 6": "队伍 6",
    "Min / Max Advances": "最小 / 最大推进",
    "Level": "等级",
    "Year": "年份",
    "Month": "月份",
    "Configuration": "配置",
    "Edit": "编辑",
    "Search": "搜索",
    "Generate": "生成",
    "Seed": "Seed",
    "Frame": "帧",
    "Nature": "性格",
    "Ability": "特性",
    "Hidden": "觉醒",
    "Power": "威力",
    "Date\\Time": "日期\\时间",
    "Keypress": "按键",
    "Keypresses": "按键",
    "Required Lead": "所需队首",
    "Lucky Power": "幸运之力",
    "Shiny Frame": "闪光帧",
    "Encounter Ratio": "遇敌比例",
    "Encounter Type": "遭遇类型",
    "Encounter Slot": "遭遇槽",
    "Synchronized": "同步",
    "C-Gear Seed": "C-Gear Seed",
    "Delay": "Delay",
}

def run_git(args: list[str]) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, encoding="utf-8").strip()

def changed_files(ref_a: str, ref_b: str) -> set[str]:
    output = run_git(["diff", "--name-only", f"{ref_a}..{ref_b}"])
    return {line.strip() for line in output.splitlines() if line.strip()}

def git_show(ref: str, path: str) -> str | None:
    try:
        return subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=ROOT, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return None

def decode_blob(blob: bytes) -> str:
    for encoding in ("utf-8-sig", "utf-8", "gb18030", "cp1252"):
        try:
            return blob.decode(encoding)
        except UnicodeDecodeError:
            continue
    return blob.decode("utf-8", errors="replace")

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")

def write_text(path: Path, text: str) -> None:
    old = path.read_text(encoding="utf-8-sig") if path.exists() else ""
    newline = "\r\n" if "\r\n" in old else "\n"
    normalized = text.replace("\r\n", "\n").replace("\r", "\n").replace("\n", newline)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(normalized, encoding="utf-8-sig")
```

- [ ] **Step 2: Implement safe file copy logic**

In `migrate_chinese_localization.py`, copy CHN versions only for files changed by CHN but not by Bambo:

```python
def copy_chn_only_files(review: list[dict[str, str]]) -> None:
    chn_changed = changed_files(BASE_REF, CHN_REF)
    target_changed = changed_files(BASE_REF, "HEAD")
    safe_files = sorted(
        path for path in chn_changed - target_changed
        if Path(path).suffix in COPY_SUFFIXES and path.startswith("RNGReporter/")
    )
    for path in safe_files:
        blob = git_show(CHN_REF, path)
        if blob is None:
            continue
        decoded = decode_blob(blob)
        write_text(ROOT / path, decoded)
        review.append({
            "path": path,
            "kind": "safe-copy",
            "english": "",
            "chinese": "Copied CHN localized file because target did not change it after merge-base.",
        })
```

- [ ] **Step 3: Implement `.resx` merge logic**

Parse matching `.resx` files, transferring CHN `<data><value>` text for keys that still exist in target:

```python
def merge_resx_file(path: str, review: list[dict[str, str]]) -> None:
    target_path = ROOT / path
    chn_blob = git_show(CHN_REF, path)
    if chn_blob is None or not target_path.exists():
        return
    try:
        target_tree = ET.parse(target_path)
        chn_root = ET.fromstring(decode_blob(chn_blob))
    except ET.ParseError:
        return
    chn_values = {}
    for data in chn_root.findall("data"):
        name = data.attrib.get("name")
        value = data.find("value")
        if name and value is not None and value.text:
            chn_values[name] = value.text
    changed = False
    for data in target_tree.getroot().findall("data"):
        name = data.attrib.get("name")
        value = data.find("value")
        if name in chn_values and value is not None and value.text != chn_values[name]:
            before = value.text or ""
            value.text = chn_values[name]
            changed = True
            review.append({"path": path, "kind": f"resx:{name}", "english": before, "chinese": chn_values[name]})
    if changed:
        target_tree.write(target_path, encoding="utf-8", xml_declaration=True)
```

- [ ] **Step 4: Implement WinForms property transfer**

Extract `this.control.Text = "..."` style assignments from CHN and target. Transfer by `(control, property)` key:

```python
PROPERTY_RE = re.compile(
    r'(?P<prefix>this\.(?P<control>[A-Za-z_][A-Za-z0-9_]*|[\u0080-\uffff][\w\u0080-\uffff]*)\.'
    r'(?P<prop>Text|HeaderText|ToolTipText|ToolTipTitle|Filter)\s*=\s*)'
    r'"(?P<value>(?:\\.|[^"\\])*)";'
)

def csharp_unescape(value: str) -> str:
    return bytes(value, "utf-8").decode("unicode_escape")

def csharp_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r")

def extract_property_values(text: str) -> dict[tuple[str, str], str]:
    result = {}
    for match in PROPERTY_RE.finditer(text):
        result[(match.group("control"), match.group("prop"))] = match.group("value")
    return result

def transfer_designer_properties(path: str, review: list[dict[str, str]]) -> None:
    target_path = ROOT / path
    chn_blob = git_show(CHN_REF, path)
    if chn_blob is None or not target_path.exists():
        return
    target_text = read_text(target_path)
    chn_text = decode_blob(chn_blob)
    chn_values = extract_property_values(chn_text)
    changed = False
    def replace(match: re.Match[str]) -> str:
        nonlocal changed
        key = (match.group("control"), match.group("prop"))
        if key not in chn_values:
            return match.group(0)
        new_value = chn_values[key]
        old_value = match.group("value")
        if old_value == new_value:
            return match.group(0)
        changed = True
        review.append({"path": path, "kind": f"{key[0]}.{key[1]}", "english": old_value, "chinese": new_value})
        return f'{match.group("prefix")}"{new_value}";'
    new_text = PROPERTY_RE.sub(replace, target_text)
    if changed:
        write_text(target_path, new_text)
```

- [ ] **Step 5: Implement manual target-only translation pass**

Apply `MANUAL_TRANSLATIONS` to designer/user-facing string assignments when no CHN equivalent exists:

```python
def apply_manual_translations(path: Path, review: list[dict[str, str]]) -> None:
    text = read_text(path)
    changed = False
    def replace(match: re.Match[str]) -> str:
        nonlocal changed
        old = match.group("value")
        if old not in MANUAL_TRANSLATIONS:
            return match.group(0)
        new = MANUAL_TRANSLATIONS[old]
        if new == old:
            return match.group(0)
        changed = True
        review.append({"path": str(path.relative_to(ROOT)).replace("\\", "/"), "kind": "manual", "english": old, "chinese": new})
        return f'{match.group("prefix")}"{csharp_escape(new)}";'
    new_text = PROPERTY_RE.sub(replace, text)
    if changed:
        write_text(path, new_text)
```

- [ ] **Step 6: Write review output**

Render review entries to `translation-review.md`:

```python
def write_review(review: list[dict[str, str]]) -> None:
    lines = [
        "# RNGReporter Chinese Localization Review",
        "",
        "请校对以下迁移或新增翻译。`safe-copy` 表示整文件来自旧汉化且目标新版未改动该文件。",
        "",
        "| File | Kind | English / Source | Chinese / Proposed |",
        "| --- | --- | --- | --- |",
    ]
    for item in review:
        english = item["english"].replace("|", "\\|").replace("\n", "<br>")
        chinese = item["chinese"].replace("|", "\\|").replace("\n", "<br>")
        lines.append(f'| `{item["path"]}` | `{item["kind"]}` | {english} | {chinese} |')
    write_text(REVIEW_PATH, "\n".join(lines) + "\n")
```

- [ ] **Step 7: Wire script main**

Run safe copies, merge conflicted resources, transfer properties, apply manual translations:

```python
def main() -> None:
    review: list[dict[str, str]] = []
    copy_chn_only_files(review)
    chn_changed = changed_files(BASE_REF, CHN_REF)
    target_changed = changed_files(BASE_REF, "HEAD")
    both_changed = sorted(chn_changed & target_changed)
    for path in both_changed:
        suffix = Path(path).suffix
        if suffix == ".resx":
            merge_resx_file(path, review)
        elif path.endswith(".Designer.cs") or path.endswith(".designer.cs") or suffix == ".cs":
            transfer_designer_properties(path, review)
    for path in (ROOT / "RNGReporter").rglob("*.cs"):
        apply_manual_translations(path, review)
    write_review(review)

if __name__ == "__main__":
    main()
```

## Task 3: Add Localization Scan Utility

**Files:**
- Create: `tools/localization/scan_localization.py`

- [ ] **Step 1: Create scan script**

Create `scan_localization.py`:

```python
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
    "Seed", "Frame", "PID", "SID", "TID", "Timer", "Timer0", "Delay", "Method",
    "HP", "Atk", "Def", "SpA", "SpD", "Spe", "RNG", "GameCube", "Cgear", "Gear",
}

def scan_conflicts() -> list[str]:
    hits = []
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".cs", ".resx", ".md", ".config"}:
            text = path.read_text(encoding="utf-8-sig", errors="ignore")
            if CONFLICT_RE.search(text):
                hits.append(str(path.relative_to(ROOT)))
    return hits

def scan_remaining_ui_english() -> list[tuple[str, str]]:
    hits = []
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
    for path, value in english[:300]:
        print(f"{path}: {value}")
    return 1 if conflicts else 0

if __name__ == "__main__":
    raise SystemExit(main())
```

## Task 4: Run Migration And Review Mechanical Output

**Files:**
- Modify: many `RNGReporter` source/resource files
- Modify: `translation-review.md`

- [ ] **Step 1: Run migration**

Run:

```powershell
python tools/localization/migrate_chinese_localization.py
```

Expected: script exits `0`, creates or updates localized files and `translation-review.md`.

- [ ] **Step 2: Inspect changed-file scope**

Run:

```powershell
git status --short
git diff --stat
```

Expected: changes are limited to localization scripts, review file, and RNGReporter localization files.

- [ ] **Step 3: Scan for conflict markers and English candidates**

Run:

```powershell
python tools/localization/scan_localization.py
```

Expected: no conflict markers. English candidates remain only where they are technical terms, intentionally preserved abbreviations, or text needing manual translation in Task 5.

## Task 5: Manually Translate Target-Only And Leftover Text

**Files:**
- Modify: `RNGReporter/Gen5FrameFinder.designer.cs`
- Modify: `RNGReporter/CgearCalibrator.Designer.cs`
- Modify: `RNGReporter/TimeFinder5th.Designer.cs`
- Modify: `RNGReporter/MainForm.Designer.cs`
- Modify: `RNGReporter/*.cs` files flagged by `scan_localization.py`
- Modify: `translation-review.md`

- [ ] **Step 1: Translate new Gen 5 Frame Finder UI**

Use these Chinese terms unless the CHN reference already supplied a different equivalent:

```text
Chatot Pitches -> 聒噪鸟音高
Possible Results: -> 可能结果:
Jump to selected frame -> 跳转到所选帧
Low -> 低
Mid-Low -> 中低
Mid -> 中
Mid-High -> 中高
High -> 高
```

- [ ] **Step 2: Translate C-Gear Calibrator UI**

Use:

```text
C-Gear Calibrator -> C-Gear 校准器
Target Seed -> 目标 Seed
Target Delay -> 目标 Delay
IV Frame -> IV 帧
RNG Info -> RNG 信息
Wild IVs -> 野生 IV
Difference -> 差值
New Delay -> 新 Delay
```

- [ ] **Step 3: Translate Pickup tab text in Time Finder 5th**

Use:

```text
Pickup -> 拾取
Target Item -> 目标道具
Notes: -> 备注:
Active Roamer -> 活动游走宝可梦
Party 1 -> 队伍 1
Party 2 -> 队伍 2
Party 3 -> 队伍 3
Party 4 -> 队伍 4
Party 5 -> 队伍 5
Party 6 -> 队伍 6
Min / Max Advances -> 最小 / 最大推进
1. Use Honey / Sweet Scent at the frame indicated, then defeat the wild Pokémon. -> 1. 在指定帧使用甜甜香气/蜂蜜，然后击败野生宝可梦。
Celestial Tower rooftop is recommended since it also has no NPCs. -> 推荐天堂之塔塔顶，因为那里也没有 NPC。
2. An "Active Roamer" (BW only) affects the initial frame. -> 2. 活动游走宝可梦（仅 BW）会影响初始帧。
3. Shiny Charm / Memory Link (BW2 only) affect the frame hit and should be accounted for. -> 3. 闪耀护符/回忆链接（仅 BW2）会影响命中帧，需要计入。
4. Wild Pokémon that have a chance of holding an item, affect the frame hit. -> 4. 可能携带道具的野生宝可梦会影响命中帧。
```

- [ ] **Step 4: Update review file with manually translated leftovers**

Append any manual translations not produced by the script to `translation-review.md` using the same table format.

## Task 6: Verification

**Files:**
- Read-only verification over entire target tree

- [ ] **Step 1: Check git state**

Run:

```powershell
git status --short --branch
```

Expected: branch is `codex/chn-localization`; changes are expected localization files only.

- [ ] **Step 2: Check for conflict markers**

Run:

```powershell
Select-String -Path (Get-ChildItem -Recurse -Include *.cs,*.resx,*.md,*.config -File).FullName -Pattern '<<<<<<<|=======|>>>>>>>'
```

Expected: no output.

- [ ] **Step 3: Run localization scan**

Run:

```powershell
python tools/localization/scan_localization.py
```

Expected: no conflict marker failures; remaining English candidates are reviewed and either translated or intentionally left.

- [ ] **Step 4: Attempt build**

Run:

```powershell
dotnet build RNGReporter.sln
```

Expected if the .NET Framework 4.8 targeting pack exists: build succeeds.

Expected if targeting pack is missing: build fails with `MSB3644` for `.NETFramework,Version=v4.8`; report this as an environment blocker and keep static verification results.

## Task 7: Commit Localization Work

**Files:**
- Commit all accepted localization changes

- [ ] **Step 1: Review diff**

Run:

```powershell
git diff --stat
git diff -- translation-review.md
```

Expected: review file is readable UTF-8 and contains校对 rows.

- [ ] **Step 2: Commit**

Run:

```powershell
git add tools/localization/migrate_chinese_localization.py tools/localization/scan_localization.py translation-review.md RNGReporter
git commit -m "Port Chinese localization to Bambo RNGReporter"
```

Expected: commit succeeds on `codex/chn-localization`.
