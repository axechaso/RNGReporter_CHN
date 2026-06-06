from __future__ import annotations

import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[2]
BASE_REF = "2c77b8eeed2a725b1b924ff3dfde2ab84e684491"
CHN_REF = "chn/master"
TARGET_REF = "origin/master"
REVIEW_PATH = ROOT / "translation-review.md"

COPY_SUFFIXES = {".cs", ".resx"}
TEXT_FILE_SUFFIXES = {".cs", ".resx", ".md", ".config"}

PROPERTY_RE = re.compile(
    r'(?P<prefix>this\.(?P<control>[A-Za-z_][A-Za-z0-9_]*|[\u0080-\uffff][\w\u0080-\uffff]*)\.'
    r'(?P<prop>Text|HeaderText|ToolTipText|ToolTipTitle|Filter)\s*=\s*)'
    r'"(?P<value>(?:\\.|[^"\\])*)";'
)
STRING_RE = re.compile(r'(?<![@\w])"(?P<value>(?:\\.|[^"\\])*)"')
CJK_RE = re.compile(r"[\u4e00-\u9fff]")

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
    "Date/Time": "日期/时间",
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
    "Item 1": "道具 1",
    "Item 2": "道具 2",
    "Item 3": "道具 3",
    "Item 4": "道具 4",
    "Item 5": "道具 5",
    "Item 6": "道具 6",
    "1. Use Honey / Sweet Scent at the frame indicated, then defeat the wild Pokémon.": "1. 在指定帧使用蜂蜜/甜甜香气，然后击败野生宝可梦。",
    "Celestial Tower rooftop is recommended since it also has no NPCs.": "推荐天堂之塔塔顶，因为那里也没有 NPC。",
    "2. An \"Active Roamer\" (BW only) affects the initial frame.": "2. 活动游走宝可梦（仅 BW）会影响初始帧。",
    "3. Shiny Charm / Memory Link (BW2 only) affect the frame hit and should be accounted for.": "3. 闪耀护符/回忆链接（仅 BW2）会影响命中帧，需要计入。",
    "4. Wild Pokémon that have a chance of holding an item, affect the frame hit.": "4. 可能携带道具的野生宝可梦会影响命中帧。",
}


@dataclass
class ReviewEntry:
    path: str
    kind: str
    source: str
    proposed: str


def run_git(args: list[str]) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, encoding="utf-8").strip()


def changed_files(ref_a: str, ref_b: str) -> set[str]:
    output = run_git(["diff", "--name-only", f"{ref_a}..{ref_b}"])
    return {line.strip() for line in output.splitlines() if line.strip()}


def git_show(ref: str, path: str) -> bytes | None:
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


def is_text_path(path: str) -> bool:
    return Path(path).suffix in TEXT_FILE_SUFFIXES and path.startswith("RNGReporter/")


def has_cjk(text: str) -> bool:
    return CJK_RE.search(text) is not None


def copy_chn_only_files(review: list[ReviewEntry]) -> None:
    chn_changed = changed_files(BASE_REF, CHN_REF)
    target_changed = changed_files(BASE_REF, TARGET_REF)
    safe_files = sorted(
        path
        for path in chn_changed - target_changed
        if path.startswith("RNGReporter/") and Path(path).suffix in COPY_SUFFIXES
    )
    for path in safe_files:
        blob = git_show(CHN_REF, path)
        if blob is None:
            continue
        write_text(ROOT / path, decode_blob(blob))
        review.append(
            ReviewEntry(
                path=path,
                kind="safe-copy",
                source="",
                proposed="整文件沿用旧汉化；Bambo 新版在分叉后未改动此文件。",
            )
        )


def parse_resx_values(text: str) -> dict[str, str]:
    try:
        root = ET.fromstring(text)
    except ET.ParseError:
        return {}
    result: dict[str, str] = {}
    for data in root.findall("data"):
        name = data.attrib.get("name")
        value = data.find("value")
        if name and value is not None and value.text is not None:
            result[name] = value.text
    return result


def merge_resx_file(path: str, review: list[ReviewEntry]) -> None:
    target_path = ROOT / path
    chn_blob = git_show(CHN_REF, path)
    if chn_blob is None or not target_path.exists():
        return
    try:
        target_tree = ET.parse(target_path)
    except ET.ParseError:
        return
    chn_values = parse_resx_values(decode_blob(chn_blob))
    if not chn_values:
        return
    changed = False
    for data in target_tree.getroot().findall("data"):
        name = data.attrib.get("name")
        value = data.find("value")
        if name not in chn_values or value is None:
            continue
        before = value.text or ""
        after = chn_values[name]
        if before == after or not has_cjk(after):
            continue
        value.text = after
        changed = True
        review.append(ReviewEntry(path=path, kind=f"resx:{name}", source=before, proposed=after))
    if changed:
        target_tree.write(target_path, encoding="utf-8", xml_declaration=True)


def extract_property_values(text: str) -> dict[tuple[str, str], str]:
    result: dict[tuple[str, str], str] = {}
    for match in PROPERTY_RE.finditer(text):
        result[(match.group("control"), match.group("prop"))] = match.group("value")
    return result


def transfer_properties(path: str, review: list[ReviewEntry]) -> None:
    target_path = ROOT / path
    chn_blob = git_show(CHN_REF, path)
    if chn_blob is None or not target_path.exists():
        return
    target_text = read_text(target_path)
    chn_values = extract_property_values(decode_blob(chn_blob))
    if not chn_values:
        return
    changed = False

    def replace(match: re.Match[str]) -> str:
        nonlocal changed
        key = (match.group("control"), match.group("prop"))
        if key not in chn_values:
            return match.group(0)
        before = match.group("value")
        after = chn_values[key]
        if before == after or not has_cjk(after):
            return match.group(0)
        changed = True
        review.append(ReviewEntry(path=path, kind=f"{key[0]}.{key[1]}", source=before, proposed=after))
        return f'{match.group("prefix")}"{after}";'

    new_text = PROPERTY_RE.sub(replace, target_text)
    if changed:
        write_text(target_path, new_text)


def extract_string_values(text: str) -> list[str]:
    return [match.group("value") for match in STRING_RE.finditer(text)]


def build_literal_map() -> dict[str, str]:
    chn_changed = changed_files(BASE_REF, CHN_REF)
    target_changed = changed_files(BASE_REF, TARGET_REF)
    candidate_files = sorted(path for path in chn_changed if is_text_path(path) and path in target_changed)
    proposed: defaultdict[str, Counter[str]] = defaultdict(Counter)
    for path in candidate_files:
        base_blob = git_show(BASE_REF, path)
        chn_blob = git_show(CHN_REF, path)
        if base_blob is None or chn_blob is None:
            continue
        base_values = extract_string_values(decode_blob(base_blob))
        chn_values = extract_string_values(decode_blob(chn_blob))
        matcher = SequenceMatcher(a=base_values, b=chn_values, autojunk=False)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == "equal":
                continue
            if tag == "replace" and (i2 - i1) == (j2 - j1):
                for before, after in zip(base_values[i1:i2], chn_values[j1:j2]):
                    if before != after and has_cjk(after):
                        proposed[before][after] += 1
    result = {}
    for before, counter in proposed.items():
        if len(counter) == 1:
            result[before] = next(iter(counter))
    result.update(MANUAL_TRANSLATIONS)
    return result


def apply_literal_map(path: Path, literal_map: dict[str, str], review: list[ReviewEntry]) -> None:
    text = read_text(path)
    changed = False
    rel = str(path.relative_to(ROOT)).replace("\\", "/")

    def replace(match: re.Match[str]) -> str:
        nonlocal changed
        before = match.group("value")
        if before not in literal_map:
            return match.group(0)
        after = literal_map[before]
        if before == after:
            return match.group(0)
        changed = True
        review.append(ReviewEntry(path=rel, kind="literal", source=before, proposed=after))
        return f'"{after}"'

    new_text = STRING_RE.sub(replace, text)
    if changed:
        write_text(path, new_text)


def write_review(review: list[ReviewEntry]) -> None:
    lines = [
        "# RNGReporter Chinese Localization Review",
        "",
        "请校对以下迁移或新增翻译。`safe-copy` 表示整文件来自旧汉化且目标新版未改动该文件。",
        "",
        "| File | Kind | English / Source | Chinese / Proposed |",
        "| --- | --- | --- | --- |",
    ]
    seen: set[tuple[str, str, str, str]] = set()
    for item in review:
        key = (item.path, item.kind, item.source, item.proposed)
        if key in seen:
            continue
        seen.add(key)
        source = item.source.replace("|", "\\|").replace("\r\n", "<br>").replace("\n", "<br>")
        proposed = item.proposed.replace("|", "\\|").replace("\r\n", "<br>").replace("\n", "<br>")
        lines.append(f"| `{item.path}` | `{item.kind}` | {source} | {proposed} |")
    write_text(REVIEW_PATH, "\n".join(lines) + "\n")


def main() -> None:
    review: list[ReviewEntry] = []
    copy_chn_only_files(review)

    chn_changed = changed_files(BASE_REF, CHN_REF)
    target_changed = changed_files(BASE_REF, TARGET_REF)
    both_changed = sorted(path for path in chn_changed & target_changed if is_text_path(path))
    for path in both_changed:
        if Path(path).suffix == ".resx":
            merge_resx_file(path, review)
        else:
            transfer_properties(path, review)

    literal_map = build_literal_map()
    for path in (ROOT / "RNGReporter").rglob("*.cs"):
        apply_literal_map(path, literal_map, review)

    write_review(review)
    print(f"review entries: {len(review)}")


if __name__ == "__main__":
    main()
