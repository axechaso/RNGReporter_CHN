from __future__ import annotations

import re
import subprocess
import codecs
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
    "C-Gear Calibrator": "Ｃ装置校准器",
    "C-Gear 校准器": "Ｃ装置校准器",
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
    "Don't Care": "任意",
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
    "Ability 0": "特性 0",
    "Ability 1": "特性 1",
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
    "C-Gear Seed": "Ｃ装置 Seed",
    "C装置Seed (16进制)": "Ｃ装置 Seed (16进制)",
    "C装置Seed帧数": "Ｃ装置 Seed 帧数",
    "C装置日期\\时间": "Ｃ装置日期\\时间",
    "C装置日期\\\\时间": "Ｃ装置日期\\\\时间",
    "C-装置Seed显示": "Ｃ装置 Seed 显示",
    "这是用来抵消普通seed和C装置seed之间时间差的数值": "这是用来抵消普通 seed 和Ｃ装置 seed 之间时间差的数值",
    "这个工具搜索C装置seed的所有可能日期，以找到与之对应的普通seed，该普通seed在多个连续帧上具有所需的性格，这将使得在连入之森捕获的宝可梦更容易获得目标性": "这个工具搜索Ｃ装置 seed 的所有可能日期，以找到与之对应的普通 seed，该普通 seed 在多个连续帧上具有所需的性格，这将使得在连入之森捕获的宝可梦更容易获得目标性",
    "Delay": "Delay",
    "This RNG handles IVs only.": "此 RNG 仅处理 IV。",
    "This RNG handles natures, gender, encounter slot, and shininess only.": "此 RNG 仅处理性格、性别、遭遇槽和闪光。",
    "Adjacent Seed Tool": "相邻 Seed 工具",
    "Base HP": "基础 HP",
    "HP": "HP",
    "Method 1": "算法 1",
    "Method J": "算法 J",
    "Method K": "算法 K",
    "Find C-Gear Seed by IVs": "通过 IV 查找 Ｃ装置 Seed",
    "通过 IV 查找 C-Gear Seed": "通过 IV 查找 Ｃ装置 Seed",
    "via PayPal": "通过 PayPal",
    "Get IVs from IVRNG (Frame 8)": "从 IVRNG 获取 IV（第 8 帧）",
    "any shiny changes from TID and SID": "任何因 TID 和 SID 造成的闪光变化",
    "Previous search running": "上一次搜索仍在运行",
    "Fishing Spot": "钓鱼点",
    "Display Parents in Search...": "在搜索中显示父母...",
    "Possible Cave Spot": "可能的洞穴尘点",
    "Possible Bubble Spot": "可能的水泡点",
    "Possible Shaking Grass": "可能的摇晃草丛",
    "Entralink Time": "连入时间",
    "Seed to Time": "Seed 转时间",
    "5th Generation Time Finder": "第五世代时间查找器",
    "4th Generation Time Finder": "第四世代时间查找器",
    "3rd Generation Time Finder": "第三世代时间查找器",
    "GameCube Time Finder": "GameCube 时间查找器",
    "Battle Trigger by Moving": "移动触发对战",
    "Gen 5 Settings": "第五世代设置",
    "Min / Max Level": "最小 / 最大等级",
    "Import Wonder Card": "导入神秘礼物",
    "International Parents": "异国",
    "Starter": "初始宝可梦",
    "Note: Use this field only if you \\nare willing to use Pass Powers \\nthrough Entralink.": "注意: 仅当你愿意通过连入\\n使用释出之力时才填写此字段。",
    "注意: 仅当你愿意通过连入之森\\n使用 Pass Power 时才填写此字段。": "注意: 仅当你愿意通过连入\\n使用释出之力时才填写此字段。",
    "Shiny Charm": "闪耀护符",
    "Lucky Power Level": "幸运之力等级",
    "Lucky Power Note": "幸运之力备注",
    "Custom": "自定义",
    "Custom 1": "自定义 1",
    "Custom 2": "自定义 2",
    "Custom 3": "自定义 3",
    "Custom 4": "自定义 4",
    "Custom 5": "自定义 5",
    "Custom 6": "自定义 6",
    "Custom 7": "自定义 7",
    "Custom 8": "自定义 8",
    "Custom 9": "自定义 9",
    "Custom 10": "自定义 10",
    "Custom1": "自定义1",
    "Custom2": "自定义2",
    "Custom3": "自定义3",
    "Custom4": "自定义4",
    "Custom5": "自定义5",
    "Custom6": "自定义6",
    "Custom7": "自定义7",
    "Custom8": "自定义8",
    "Custom9": "自定义9",
    "Custom10": "自定义10",
    "32BitHigh": "32位高位",
    "32BitLow": "32位低位",
    "16BitHigh": "16位高位",
    "16BitLow": "16位低位",
    "E - Hearing about your escapades rocks my soul! It sure does!": "E - 听说你的冒险事迹真让我热血沸腾！确实如此！",
    "First 10 IVs in Seed:": "Seed 的前 10 个 IV:",
    "Delays": "Delay",
    "Lower Half PID": "PID 低半部分",
    "Suction Cups": "吸盘",
    "Compoundeyes": "复眼",
    "IV filters are set for fast searching.": "IV 筛选已设置为快速搜索。",
    "Copy C-Gear Seed to Clipboard": "复制 Ｃ装置 Seed 到剪贴板",
    "Calibrate C-Gear Delay by Wild IVs": "通过野生 IV 校准 Ｃ装置 Delay",
    "复制 C-Gear Seed 到剪贴板": "复制 Ｃ装置 Seed 到剪贴板",
    "通过野生 IV 校准 C-Gear Delay": "通过野生 IV 校准 Ｃ装置 Delay",
    "Preferences": "偏好",
    "Battle Trigger": "对战触发",
    "Settings": "设置",
    "Calibrate Delay": "校准 Delay",
    "Gender": "性别",
    "Import": "导入",
    "Event TID / SID": "活动 TID / SID",
    "Gender Ratio": "性别比例",
    "2. An \\\"Active Roamer\\\" (BW only) affects the initial frame.": "2. 活动游走宝可梦（仅 BW）会影响初始帧。",
    "Stage One": "第一阶段",
    "Countdown Beep": "倒计时提示音",
    "seconds": "秒",
    "Stage Two": "第二阶段",
    "frames": "帧",
    "START": "开始",
    "Game Entry Seconds (4th Gen)": "进入游戏秒数（第四世代）",
    "Two-Stage Timer": "双阶段计时器",
    "Heart Gold\\\\Soul Silver": "心金\\\\魂银",
    "Diamond\\\\Pearl\\\\Platinum": "钻石\\\\珍珠\\\\白金",
    "✨Patch Frame": "✨补丁帧",
    "BOLD.": "加粗。",
    "Offset": "偏移",
    "Item 1": "道具 1",
    "Item 2": "道具 2",
    "Item 3": "道具 3",
    "Item 4": "道具 4",
    "Item 5": "道具 5",
    "Item 6": "道具 6",
    "1. Use Honey / Sweet Scent at the frame indicated, then defeat the wild Pokémon.": "1. 在指定帧使用甜甜蜜/甜甜香气，然后击败野生宝可梦。",
    "1. 在指定帧使用蜂蜜/甜甜香气，然后击败野生宝可梦。": "1. 在指定帧使用甜甜蜜/甜甜香气，然后击败野生宝可梦。",
    "输入在开启C装置之后立即捕捉到的宝可梦的个体值": "输入在开启Ｃ装置之后立即捕捉到的宝可梦的个体值",
    "GEN5（非C装置）": "GEN5（非Ｃ装置）",
    "GEN5（C装置）": "GEN5（Ｃ装置）",
    "BW（C装置Seed）": "BW（Ｃ装置 Seed）",
    "GEN5个体值（C装置Seed）": "GEN5个体值（Ｃ装置 Seed）",
    "Seed to Time (C装置 Seeds)": "Seed 转时间（Ｃ装置 Seeds）",
    "Celestial Tower rooftop is recommended since it also has no NPCs.": "推荐天堂之塔塔顶，因为那里也没有 NPC。",
    "2. An \"Active Roamer\" (BW only) affects the initial frame.": "2. 活动游走宝可梦（仅 BW）会影响初始帧。",
    "3. Shiny Charm / Memory Link (BW2 only) affect the frame hit and should be accounted for.": "3. 闪耀护符/记忆连接（仅 BW2）会影响命中帧，需要计入。",
    "4. Wild Pokémon that have a chance of holding an item, affect the frame hit.": "4. 可能携带道具的野生宝可梦会影响命中帧。",
    "Unsupported for now.": "暂不支持。",
    "Your MAC address is missing some digits.  Double-check your MAC address.": "MAC 地址缺少部分数字，请再次检查 MAC 地址。",
    "Please select a specific list of natures.": "请选择具体的性格列表。",
    "Year must be a value between 2000 and 2099, inclusive.": "年份必须是 2000 到 2099 之间的值（含端点）。",
    "HP: Lower limit > Upper limit": "HP：下限 > 上限",
    "Atk: Lower limit > Upper limit": "攻击：下限 > 上限",
    "Def: Lower limit > Upper limit": "防御：下限 > 上限",
    "SpA: Lower limit > Upper limit": "特攻：下限 > 上限",
    "SpD: Lower limit > Upper limit": "特防：下限 > 上限",
    "Spe: Lower limit > Upper limit": "速度：下限 > 上限",
    "You need to select a target frame in the preview!": "你需要在预览中选择目标帧！",
    "RNG Reporter now has a new profile manager.\\r\\nPlease save your information in a profile.": "RNG Reporter 现在有新的存档信息管理器。\\r\\n请将你的信息保存到存档信息中。",
    "Your version of RNG Reporter is outdated.  The latest version is ": "你的 RNG Reporter 版本已过期。最新版本是 ",
    "What's new: ": "新内容：",
    "Would you like to download and install the latest version now?": "是否立即下载并安装最新版本？",
    "You need to adjust settings in Time Finder first.": "你需要先在 Time Finder 中调整设置。",
    "This method requires you to copy the Full Seed from the Time Finder window.": "此方法需要你从 Time Finder 窗口复制 Full Seed。",
    "You need to import a Wonder Card (.pgf file) first. Import one now?": "你需要先导入神秘礼物（.pgf 文件）。现在导入吗？",
    "Cannot display Japanese without a Japanese-supported font.": "没有支持日文的字体，无法显示日文。",
    "Cannot display Korean without a Korean-supported font.": "没有支持韩文的字体，无法显示韩文。",
    "Unsupported Language": "不支持的语言",
    "Wonder Card loaded successfully:": "神秘礼物加载成功：",
    "Wonder Card": "神秘礼物",
    "5th Gen Wonder Card |*.pgf": "第五世代神秘礼物 |*.pgf",
    "Select a Wonder Card File": "选择神秘礼物文件",
    "TXT Files|*.txt": "TXT 文件|*.txt",
    "XML Profiles|*.xml|All files|*.*": "XML 存档信息|*.xml|所有文件|*.*",
    "Save Output to TXT": "保存输出到 TXT",
    "Open Researcher Profile": "打开 Researcher 配置",
    "????? TXT": "保存输出到 TXT",
    "?? Researcher ??": "打开 Researcher 配置",
    "Random": "随机",
    "Male": "雄性",
    "Female": "雌性",
    "May be Shiny": "可能闪光",
    "Info": "信息",
    "Nature: ": "性格: ",
    "Ability: ": "特性: ",
    "Gender: ": "性别: ",
    "Shininess: ": "闪光: ",
    "HP: ": "HP: ",
    "Atk: ": "攻击: ",
    "Def: ": "防御: ",
    "SpA: ": "特攻: ",
    "SpD: ": "特防: ",
    "Spe: ": "速度: ",
    "You do not have enough free memory to load {0} for the fast egg search.": "可用内存不足，无法为快速蛋搜索加载 {0}。",
    "Problem loading {0} for the fast egg search:\\r\\n{1}": "为快速蛋搜索加载 {0} 时出现问题：\\r\\n{1}",
    "Corrupt or old format profiles detected. Unable to load.": "检测到损坏或旧格式的存档信息，无法加载。",
    "It's impossible to hit hollow number {0} with {1} open hollows!": "有 {1} 个开放隐藏洞穴时无法命中第 {0} 个洞穴！",
    "Many thanks to:": "特别感谢：",
    "TCCPhreak, for the major research into Trainer ID generation": "TCCPhreak，感谢其对训练家 ID 生成的主要研究",
    "LightningFusion, for providing a sample seed/ID combo for testing": "LightningFusion，感谢其提供用于测试的 Seed/ID 示例组合",
    "mingot, for an easy way to search only viable seeds and other valuable coding advice": "mingot，感谢其提供只搜索可行 Seed 的简便方法和其他宝贵编码建议",
    "http://hocomcast.net/~charltoncr/mt19937ar.htm for providing Mersenne Twister Code": "http://hocomcast.net/~charltoncr/mt19937ar.htm，感谢其提供 Mersenne Twister 代码",
    "You, for downloading and enjoying this program": "你，感谢你下载并使用这个程序",
    "Credits!": "鸣谢！",
    "The previous search is still running.": "上一次搜索仍在运行。",
    "IDs can only be between 0 and 65535": "ID 只能在 0 到 65535 之间",
    "No matches found for the IVs entered.  Please check and try again.": "未找到与输入 IV 匹配的结果，请检查后重试。",
    "No Data Found": "未找到数据",
    "No reasonable initial seed found. Please check your DATE and TIME.": "未找到合理的初始 seed。请检查日期和时间。",
    "There was a problem with the stats/nature/Pokemon you have entered.  Please check them and try again.  ": "你输入的能力值、性格或宝可梦有问题。请检查后重试。",
    "There was a problem with the stats/nature/Pokemon you have entered.  Please check them and try again. ": "你输入的能力值、性格或宝可梦有问题。请检查后重试。",
    "Invalid Stats": "能力值无效",
    "To many IV Combinations": "IV 组合过多",
    "You must enter a year.": "你必须输入年份。",
    "Please Enter a Year": "请输入年份",
    "You must enter a seconds value.": "你必须输入秒数。",
    "Please Enter Seconds": "请输入秒数",
    "No match was found for your flips.": "未找到匹配的翻硬币结果。",
    "No Match": "未找到匹配项",
    "No match was found for your Elm responses.": "未找到匹配的空木博士响应。",
    "No match was found for your IVs.": "未找到匹配的 IV。",
    "No match was found for your Roaming Pokemon.": "未找到匹配的游走宝可梦。",
    "The parent IVs you have listed cannot produce your desired search results.": "你列出的父母 IV 无法产生期望的搜索结果。",
    "You must enter a year greater than 1999.": "你必须输入大于 1999 的年份。",
    "This method is not possible in BW2.": "此方法在 BW2 中不可用。",
    "error in loading roamer tables": "加载游走宝可梦表时出错",
    "Currently not supported for this method.": "当前不支持此方法。",
    "Loading the seeds file. Please be patient and wait for it to finish.": "正在加载 seed 文件，请耐心等待完成。",
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
    return decode_blob(path.read_bytes())


def write_text(path: Path, text: str) -> None:
    normalized = (
        text.replace("\r\r\n", "\n")
        .replace("\r\n", "\n")
        .replace("\r", "\n")
    )
    normalized = "\n".join(line.rstrip(" \t") for line in normalized.split("\n"))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(codecs.BOM_UTF8 + normalized.encode("utf-8"))


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
        "## 术语基准",
        "",
        "宝可梦专有名词优先对齐 52Poké / 神奇宝贝百科；RNG 工具术语如 `Seed`、`Frame`、`Delay`、`PID`、`SID`、`TID`、`IV`、`HP` 保留社区常用写法。",
        "",
        "- `C-Gear` -> `Ｃ装置`: https://wiki.52poke.com/wiki/%EF%BC%A3%E8%A3%85%E7%BD%AE",
        "- `Entralink` -> `连入`, `Entree Forest` -> `连入之森`, `Pass Power` -> `释出之力`: https://wiki.52poke.com/wiki/%E8%BF%9E%E5%85%A5",
        "- `Chatot` -> `聒噪鸟`: https://wiki.52poke.com/wiki/%E8%81%92%E5%99%AA%E9%B8%9F",
        "- `Honey` -> `甜甜蜜`: https://wiki.52poke.com/wiki/%E7%94%9C%E7%94%9C%E8%9C%9C%EF%BC%88%E9%81%93%E5%85%B7%EF%BC%89",
        "- `Sweet Scent` -> `甜甜香气`: https://wiki.52poke.com/wiki/%E7%94%9C%E7%94%9C%E9%A6%99%E6%B0%94%EF%BC%88%E6%8B%9B%E5%BC%8F%EF%BC%89",
        "- `Shiny Charm` -> `闪耀护符`: https://wiki.52poke.com/wiki/%E9%97%AA%E8%80%80%E6%8A%A4%E7%AC%A6%EF%BC%88%E9%81%93%E5%85%B7%EF%BC%89",
        "- `Celestial Tower` -> `天堂之塔`: https://wiki.52poke.com/wiki/%E5%A4%A9%E5%A0%82%E4%B9%8B%E5%A1%94",
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


def changed_worktree_files() -> list[str]:
    output = run_git(["diff", "--name-only", TARGET_REF, "--", "RNGReporter"])
    return [line.strip() for line in output.splitlines() if line.strip()]


def build_current_review() -> list[ReviewEntry]:
    review: list[ReviewEntry] = []
    seen: set[tuple[str, str, str, str]] = set()

    def add(entry: ReviewEntry) -> None:
        key = (entry.path, entry.kind, entry.source, entry.proposed)
        if key in seen:
            return
        seen.add(key)
        review.append(entry)

    for path in changed_worktree_files():
        target_path = ROOT / path
        if not target_path.exists() or Path(path).suffix not in TEXT_FILE_SUFFIXES:
            continue
        old_blob = git_show(TARGET_REF, path)
        if old_blob is None:
            continue
        old_text = decode_blob(old_blob)
        new_text = read_text(target_path)

        if Path(path).suffix == ".resx":
            old_values = parse_resx_values(old_text)
            new_values = parse_resx_values(new_text)
            for name, before in old_values.items():
                after = new_values.get(name)
                if after and before != after and (has_cjk(after) or before in MANUAL_TRANSLATIONS):
                    add(ReviewEntry(path=path, kind=f"resx:{name}", source=before, proposed=after))
            continue

        old_props = extract_property_values(old_text)
        new_props = extract_property_values(new_text)
        for key, before in old_props.items():
            after = new_props.get(key)
            if after and before != after and (has_cjk(after) or before in MANUAL_TRANSLATIONS):
                add(ReviewEntry(path=path, kind=f"{key[0]}.{key[1]}", source=before, proposed=after))

        old_literals = extract_string_values(old_text)
        new_literals = extract_string_values(new_text)
        matcher = SequenceMatcher(a=old_literals, b=new_literals, autojunk=False)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == "equal" or (i2 - i1) != (j2 - j1):
                continue
            for before, after in zip(old_literals[i1:i2], new_literals[j1:j2]):
                if before != after and (has_cjk(after) or before in MANUAL_TRANSLATIONS):
                    add(ReviewEntry(path=path, kind="literal", source=before, proposed=after))
    return review


def apply_compile_safety_fixes() -> None:
    replacements = {
        "RNGReporter/JirachiGeneration.cs": [
            ("                可能值Probable = result", "                Probable = result"),
        ],
        "RNGReporter/PIDToIVs.cs": [
            ("算法 =", "Method ="),
            ("个体值 =", "IVs ="),
            ("frame.算法", "frame.Method"),
            ("frame.个体值", "frame.IVs"),
        ],
        "RNGReporter/DSIDWizard.Designer.cs": [
            ("            this.dataGridView1.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridView1_CellContentClick);\n", ""),
        ],
        "RNGReporter/SeedFinder.Designer.cs": [
            ("            this.label3.Click += new System.EventHandler(this.label3_Click);\n", ""),
        ],
    }
    for relative, fixes in replacements.items():
        target_path = ROOT / relative
        if not target_path.exists():
            continue
        text = read_text(target_path)
        for source, target in fixes:
            text = text.replace(source, target)
        write_text(target_path, text)


def apply_source_identity_fixes() -> None:
    protected_literals = {"HP"}
    for path in changed_worktree_files():
        target_path = ROOT / path
        if not target_path.exists() or Path(path).suffix not in TEXT_FILE_SUFFIXES:
            continue
        old_blob = git_show(TARGET_REF, path)
        if old_blob is None:
            continue
        old_values = extract_string_values(decode_blob(old_blob))
        text = read_text(target_path)
        new_matches = list(STRING_RE.finditer(text))
        new_values = [match.group("value") for match in new_matches]
        replacements: list[tuple[int, int, str]] = []
        matcher = SequenceMatcher(a=old_values, b=new_values, autojunk=False)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if (i2 - i1) != (j2 - j1):
                continue
            for before, match in zip(old_values[i1:i2], new_matches[j1:j2]):
                if before in protected_literals and match.group("value") != before:
                    replacements.append((match.start("value"), match.end("value"), before))
        if not replacements:
            continue
        chars = list(text)
        for start, end, value in reversed(replacements):
            chars[start:end] = value
        write_text(target_path, "".join(chars))


def replace_string_value(text: str, control: str, prop: str, value: str) -> str:
    pattern = re.compile(rf'(this\.{re.escape(control)}\.{re.escape(prop)}\s*=\s*)"(?:\\.|[^"\\])*";')
    return pattern.sub(lambda match: f'{match.group(1)}"{value}";', text)


def replace_point(text: str, control: str, x: int, y: int) -> str:
    pattern = re.compile(rf'(this\.{re.escape(control)}\.Location\s*=\s*new System\.Drawing\.Point\()\d+, \d+(\);)')
    return pattern.sub(lambda match: f'{match.group(1)}{x}, {y}{match.group(2)}', text)


def replace_size(text: str, control: str, width: int, height: int) -> str:
    pattern = re.compile(rf'(this\.{re.escape(control)}\.Size\s*=\s*new System\.Drawing\.Size\()\d+, \d+(\);)')
    return pattern.sub(lambda match: f'{match.group(1)}{width}, {height}{match.group(2)}', text)


def replace_autosize(text: str, control: str, value: bool) -> str:
    pattern = re.compile(rf'(this\.{re.escape(control)}\.AutoSize\s*=\s*)(?:true|false)(;)')
    return pattern.sub(lambda match: f'{match.group(1)}{str(value).lower()}{match.group(2)}', text)


def ensure_text_align(text: str, control: str, align: str) -> str:
    text = re.sub(
        rf'(this\.{re.escape(control)}\.TextAlign\s*=\s*System\.Drawing\.ContentAlignment\.)[A-Za-z]+;',
        rf'\1{align};',
        text,
    )
    if f'this.{control}.TextAlign' in text:
        return text
    pattern = re.compile(rf'(this\.{re.escape(control)}\.Text\s*=\s*"(?:\\.|[^"\\])*";\n)')
    return pattern.sub(lambda match: match.group(1) + f'            this.{control}.TextAlign = System.Drawing.ContentAlignment.{align};\n', text, count=1)


def apply_main_form_layout_fixes() -> None:
    path = ROOT / "RNGReporter/MainForm.Designer.cs"
    text = read_text(path)
    for control, y in (("label3", 53), ("label12", 160), ("label11", 185), ("label4", 211)):
        text = replace_autosize(text, control, False)
        text = replace_point(text, control, 9, y - 2)
        text = replace_size(text, control, 88, 18)
        text = ensure_text_align(text, control, "MiddleRight")
    text = replace_string_value(text, "HP", "HeaderText", "HP")
    text = replace_string_value(text, "HP", "Name", "HP")
    text = replace_string_value(text, "label19", "Text", "Elm\u7535\u8bdd\u83b7\u53d6Seed\uFF1A")
    text = replace_point(text, "label19", 390, 548)
    text = replace_size(text, "label19", 108, 13)
    text = replace_point(text, "labelElmForSeed", 500, 548)
    text = replace_string_value(text, "checkBoxLPresent", "Text", "\u62c9\u5e1d\u4e9a\u65af/\u62c9\u5e1d\u6b27\u65af")
    text = replace_size(text, "checkBoxLPresent", 128, 17)
    text = replace_string_value(text, "label18", "Text", "\u6e38\u8d70\u4f4d\u7f6e\uFF1A")
    text = replace_point(text, "label18", 455, 573)
    text = replace_size(text, "label18", 70, 13)
    text = replace_point(text, "labelRoamerRoutes", 525, 573)
    write_text(path, text)


def apply_iv_filters_fixes() -> None:
    path = ROOT / "RNGReporter/Controls/IVFilters.Designer.cs"
    text = read_text(path)
    items = '"\u65e0",\n            "==",\n            ">=",\n            "<=",\n            "!=",\n            "\u5076",\n            "\u5947",\n            "HP",\n            "HP\u5076",\n            "HP\u5947"'
    pattern = re.compile(r'(this\.cb(?:Spe|HP|Atk|Def|SpA|SpD)\.Items\.AddRange\(new object\[\] \{\n)(.*?)(\}\);)', re.S)
    text = pattern.sub(lambda match: match.group(1) + '            ' + items + match.group(3), text)
    for control in ("lblHP",):
        text = replace_string_value(text, control, "Text", "HP")
    write_text(path, text)


def apply_timefinder4th_layout_fixes() -> None:
    path = ROOT / "RNGReporter/TimeFinder4th.Designer.cs"
    text = read_text(path)
    text = replace_string_value(text, "checkBoxIntlParents", "Text", "\u5f02\u56fd")
    text = replace_size(text, "checkBoxIntlParents", 62, 17)
    text = replace_string_value(text, "label11", "Text", "HP")
    text = replace_point(text, "label92", 625, 94)
    text = replace_size(text, "label92", 68, 13)
    text = text.replace(
        'this.labelDPPtWarning.Text = "Please note that number of flips and taps that are listed assume that you will al" +\n    "so be doing 10 coin flips to verify your initial seed. ";',
        'this.labelDPPtWarning.Text = "\u8bf7\u6ce8\u610f\uFF1A\u5217\u51fa\u7684\u6295\u5e01\u548c\u8f7b\u89e6\u6b21\u6570\u5047\u5b9a\u4f60\u8fd8\u4f1a\u989d\u5916\u6295 10 \u6b21\u786c\u5e01\u6765\u786e\u8ba4\u521d\u59cb Seed\u3002";'
    )
    text = text.replace(
        'this.labelHappinessWarning.Text = "It also assumes that you start the game from the coin flip application, and then " +\n    "switch to the happiness checker application.\\r\\n";',
        'this.labelHappinessWarning.Text = "\u8fd8\u5047\u5b9a\u4f60\u4ece\u6295\u5e01\u5e94\u7528\u5f00\u59cb\u6e38\u620f\uff0c\u7136\u540e\u5207\u6362\u5230\u4eb2\u5bc6\u5ea6\u68c0\u6d4b\u5668\u5e94\u7528\u3002";'
    )
    write_text(path, text)


def apply_timefinder5th_wording_fixes() -> None:
    path = ROOT / "RNGReporter/TimeFinder5th.Designer.cs"
    if not path.exists():
        return
    text = read_text(path)
    text = replace_string_value(text, "checkBoxIntlParents", "Text", "\u5f02\u56fd")
    text = replace_size(text, "checkBoxIntlParents", 62, 17)
    write_text(path, text)


def replace_items_array(text: str, control: str, items: list[str]) -> str:
    rendered = ",\n".join(f'            "{item}"' for item in items)
    pattern = re.compile(
        rf'(this\.{re.escape(control)}\.Items\.AddRange\(new object\[\] \{{\n)(.*?)(\}}\);)',
        re.S,
    )
    return pattern.sub(lambda match: match.group(1) + rendered + match.group(3), text)


def set_grid_header_font(text: str, grid: str, family: str = "\u5b8b\u4f53", size: str = "9F") -> str:
    pattern = re.compile(
        rf'(dataGridViewCellStyle\d+\.Font\s*=\s*new System\.Drawing\.Font\()'
        rf'"[^"]+", [^;]+(;\n(?:(?!dataGridViewCellStyle\d+\.Font\s*=).)*?'
        rf'this\.{re.escape(grid)}\.ColumnHeadersDefaultCellStyle\s*=)',
        re.S,
    )
    return pattern.sub(
        lambda match: f'{match.group(1)}"{family}", {size}, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0))){match.group(2)}',
        text,
    )


def apply_timefinder3rd_layout_fixes() -> None:
    path = ROOT / "RNGReporter/TimeFinder3rd.Designer.cs"
    text = read_text(path)
    compatibility_items = [
        "\u4e24\u53ea\u5b9d\u53ef\u68a6\u4e0d\u592a\u559c\u6b22\u5bf9\u65b9",
        "\u4e24\u53ea\u5b9d\u53ef\u68a6\u5173\u7cfb\u4e0d\u9519",
        "\u4e24\u53ea\u5b9d\u53ef\u68a6\u5173\u7cfb\u975e\u5e38\u597d",
    ]
    for control in ("comboEPIDCompatibility", "comboBoxParentCompatibility", "compatibilityFRLG"):
        text = replace_items_array(text, control, compatibility_items)
        text = replace_size(text, control, 242, 21)

    gender_items = [
        "\u4e0d\u8003\u8651/\u56fa\u5b9a\u6027\u522b/\u65e0\u6027\u522b",
        "\u96cc\uff0850% \u96c4 / 50% \u96cc\uff09",
        "\u96c4\uff0850% \u96c4 / 50% \u96cc\uff09",
        "\u96cc\uff0825% \u96c4 / 75% \u96cc\uff09",
        "\u96c4\uff0825% \u96c4 / 75% \u96cc\uff09",
        "\u96cc\uff0875% \u96c4 / 25% \u96cc\uff09",
        "\u96c4\uff0875% \u96c4 / 25% \u96cc\uff09",
        "\u96cc\uff0887.5% \u96c4 / 12.5% \u96cc\uff09",
        "\u96c4\uff0887.5% \u96c4 / 12.5% \u96cc\uff09",
    ]
    for control in ("comboEPIDGender", "comboBoxShiny3rdGender", "glassComboBoxGenderFRLG", "comboBoxGender"):
        text = replace_items_array(text, control, gender_items)
        text = replace_size(text, control, 250, 21)

    for control, x, y, width in (
        ("label3", 620, 77, 68),
        ("label20", 620, 131, 68),
        ("label23", 650, 27, 38),
        ("label24", 650, 52, 38),
        ("label1", 620, 104, 68),
        ("label41", 268, 63, 68),
        ("label58", 16, 130, 68),
        ("label65", 300, 13, 36),
        ("label71", 300, 39, 36),
        ("label61", 16, 130, 68),
    ):
        text = replace_autosize(text, control, False)
        text = replace_point(text, control, x, y)
        text = replace_size(text, control, width, 18)
        text = ensure_text_align(text, control, "MiddleRight")

    for control in ("label42", "label59"):
        text = replace_string_value(text, control, "Text", "HP")
    for control in ("shiny3rdHP", "dataGridViewTextBoxColumn50"):
        text = replace_string_value(text, control, "HeaderText", "HP")

    width_fixes = {
        "shiny3rdHP": 36,
        "shiny3rdAtk": 36,
        "shiny3rdDef": 36,
        "shiny3rdSpA": 36,
        "shiny3rdSpD": 36,
        "shiny3rdSpe": 36,
        "dataGridViewTextBoxColumn50": 36,
        "dataGridViewTextBoxColumn51": 36,
        "dataGridViewTextBoxColumn52": 36,
        "dataGridViewTextBoxColumn53": 36,
        "dataGridViewTextBoxColumn54": 36,
        "dataGridViewTextBoxColumn55": 36,
    }
    for control, width in width_fixes.items():
        text = re.sub(
            rf'(this\.{re.escape(control)}\.Width\s*=\s*)\d+(;)',
            rf'\g<1>{width}\2',
            text,
        )

    text = set_grid_header_font(text, "dataGridViewEPIDs", size="9F")
    text = set_grid_header_font(text, "dataGridViewShinyRSResults", size="9F")
    text = set_grid_header_font(text, "dataGridFRLG", size="9F")
    write_text(path, text)


def apply_timefinder3rd_runtime_fixes() -> None:
    path = ROOT / "RNGReporter/TimeFinder3rd.cs"
    text = read_text(path)
    replacements = {
        'new ComboBoxItem("Ability 0", 0)': 'new ComboBoxItem("\u7279\u6027 0", 0)',
        'new ComboBoxItem("Ability 1", 1)': 'new ComboBoxItem("\u7279\u6027 1", 1)',
        'new ComboBoxItem("Method 1", FrameType.Method1)': 'new ComboBoxItem("\u7b97\u6cd5 1", FrameType.Method1)',
        'new ComboBoxItem("Method 2", FrameType.Method2)': 'new ComboBoxItem("\u7b97\u6cd5 2", FrameType.Method2)',
        'new ComboBoxItem("Method 4", FrameType.Method4)': 'new ComboBoxItem("\u7b97\u6cd5 4", FrameType.Method4)',
        'new ComboBoxItem("Method H-1", FrameType.MethodH1)': 'new ComboBoxItem("\u7b97\u6cd5 H-1", FrameType.MethodH1)',
        'new ComboBoxItem("Method H-2", FrameType.MethodH2)': 'new ComboBoxItem("\u7b97\u6cd5 H-2", FrameType.MethodH2)',
        'new ComboBoxItem("Method H-4", FrameType.MethodH4)': 'new ComboBoxItem("\u7b97\u6cd5 H-4", FrameType.MethodH4)',
        'new ComboBoxItem("Wild Pok\u00e9mon (Surfing)",': 'new ComboBoxItem("\u91ce\u751f\u5b9d\u53ef\u68a6\uff08\u51b2\u6d6a\uff09",',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    write_text(path, text)


def apply_timefinder4th_runtime_fixes() -> None:
    path = ROOT / "RNGReporter/TimeFinder4th.cs"
    text = read_text(path)
    replacements = {
        'new ComboBoxItem("Method 1", FrameType.Method1)': 'new ComboBoxItem("\u7b97\u6cd5 1", FrameType.Method1)',
        'new ComboBoxItem("Method J", FrameType.MethodJ)': 'new ComboBoxItem("\u7b97\u6cd5 J", FrameType.MethodJ)',
        'new ComboBoxItem("Method K", FrameType.MethodK)': 'new ComboBoxItem("\u7b97\u6cd5 K", FrameType.MethodK)',
        'new ComboBoxItem("Wondercard IVs", FrameType.WondercardIVs)': 'new ComboBoxItem("\u795e\u79d8\u793c\u7269 IV", FrameType.WondercardIVs)',
        'new ComboBoxItem("\u795e\u79d8\u5361\u7247 IV", FrameType.WondercardIVs)': 'new ComboBoxItem("\u795e\u79d8\u793c\u7269 IV", FrameType.WondercardIVs)',
        'new ComboBoxItem("PokeWalker IVs", FrameType.WondercardIVs)': 'new ComboBoxItem("\u5b9d\u53ef\u8ba1\u6b65\u5668 IV", FrameType.WondercardIVs)',
        'new ComboBoxItem("Chained Spreads", FrameType.ChainedShiny)': 'new ComboBoxItem("\u8fde\u9501\u5f02\u8272", FrameType.ChainedShiny)',
        '"Wild Pok\u00e9mon (Surfing)"': '"\u91ce\u751f\u5b9d\u53ef\u68a6\uff08\u51b2\u6d6a\uff09"',
        '"Bug-Catching Contest"': '"\u6355\u866b\u5927\u8d5b"',
        'new ComboBoxItem("Ability 0", 0)': 'new ComboBoxItem("\u7279\u6027 0", 0)',
        'new ComboBoxItem("Ability 1", 1)': 'new ComboBoxItem("\u7279\u6027 1", 1)',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    write_text(path, text)


def apply_encounter_string_fixes() -> None:
    path = ROOT / "RNGReporter/Objects/EncounterMods.cs"
    text = read_text(path)
    text = text.replace('case "Wild Pok\u00e9mon (Surfing)":', 'case "\u91ce\u751f\u5b9d\u53ef\u68a6\uff08\u51b2\u6d6a\uff09":')
    text = text.replace('case "Bug-Catching Contest":', 'case "\u6355\u866b\u5927\u8d5b":')
    extra_cases = {
        "草丛": "Wild",
        "深色草丛": "WildDarkGrass",
        "大量出现": "WildSwarm",
        "冲浪": "WildSurfing",
        "垂钓": "WildSuperRod",
        "飞行影子": "WildShadow",
        "游走宝可梦": "Roamer",
        "燃烧虫/小福蛋的蛋": "LarvestaHappiny",
        "胖嘟嘟": "JellicentHA",
    }
    marker = '                case "Wild Pokémon (Tall Grass)":\n'
    if marker in text and 'case "草丛":' not in text:
        rendered = "".join(
            f'                case "{label}":\n                    return EncounterType.{enum_name};\n'
            for label, enum_name in extra_cases.items()
        )
        text = text.replace(marker, rendered + marker)
    write_text(path, text)


def apply_language_defaults_fixes() -> None:
    functions_path = ROOT / "RNGReporter/Objects/Functions.cs"
    text = read_text(functions_path)
    text = text.replace("return Translations.powerENG[type];", "return Translations.powerCHS[type];")
    text = text.replace("return Translations.NatureStringENG[nature];", "return Translations.NatureStringCHS[nature];")
    text = text.replace("return Translations.encounterItemsENG[slot - 12];", "return Translations.encounterItemsCHS[slot - 12];")
    text = text.replace("return Translations.characteristicStringsENG[index];", "return Translations.characteristicStringsCHS[index];")
    write_text(functions_path, text)

    pokemon_path = ROOT / "RNGReporter/Objects/Pokemon.cs"
    text = read_text(pokemon_path)
    text = text.replace("return Translations.pokemonNamesENG[index];", "return Translations.pokemonNamesCHS[index];")
    text = text.replace("return Translations.abilityNameENG[ability];", "return Translations.abilityNameCHS[ability];")
    write_text(pokemon_path, text)

    characteristic_path = ROOT / "RNGReporter/Objects/Characteristic.cs"
    text = read_text(characteristic_path).replace('"NONE"', '"无"')
    write_text(characteristic_path, text)

    for relative in ("RNGReporter/DexIVCheck.cs", "RNGReporter/DSParametersIVCheck.cs"):
        path = ROOT / relative
        text = read_text(path)
        text = re.sub(
            r'Characteristic characteristic = null;\s*'
            r'if \(comboBoxCharacteristic\.SelectedItem\.ToString\(\) != "NONE"\)\s*'
            r'\{\s*characteristic = \(Characteristic\)\s*comboBoxCharacteristic\.SelectedItem;\s*\}',
            'Characteristic characteristic = comboBoxCharacteristic.SelectedItem as Characteristic;',
            text,
            flags=re.S,
        )
        text = re.sub(
            r'default:\s*\n\s*font = DefaultFont;\s*\n\s*break;',
            'default:\n                    font = new Font("Microsoft YaHei UI", 9F);\n                    if (font.Name != "Microsoft YaHei UI")\n                    {\n                        font = new Font("宋体", 9F);\n                    }\n                    break;',
            text,
        )
        write_text(path, text)


def apply_settings_designer_key_fixes() -> None:
    settings_path = ROOT / "RNGReporter/Properties/Settings.settings"
    designer_path = ROOT / "RNGReporter/Properties/Settings.Designer.cs"
    ns = {"s": "http://schemas.microsoft.com/VisualStudio/2004/01/settings"}
    root = ET.fromstring(read_text(settings_path))
    names = [
        node.attrib["Name"]
        for node in root.findall(".//s:Setting", ns)
        if node.attrib.get("Name")
    ]
    text = read_text(designer_path)
    for name in names:
        pattern = re.compile(
            rf'(public\s+[\w:.\[\]<>]+\s+{re.escape(name)}\s*\{{.*?'
            rf'return \(\([^)]*\)\(this\[)[^\]]*(\]\)\);\s*\}}\s*'
            rf'set\s*\{{\s*this\[)[^\]]*(\]\s*=\s*value;\s*\}}\s*\}})',
            re.S,
        )
        text = pattern.sub(lambda match, setting=name: f'{match.group(1)}"{setting}"{match.group(2)}"{setting}"{match.group(3)}', text)
    write_text(designer_path, text)


def apply_seed_finder_fixes() -> None:
    path = ROOT / "RNGReporter/SeedFinder.Designer.cs"
    text = read_text(path)
    text = re.sub(
        r'this\.Font = new System\.Drawing\.Font\("[^"]+", [^;]+;',
        'this.Font = new System.Drawing.Font("Microsoft YaHei UI", 9F);',
        text,
    )
    for grid in ("dataGridViewValues", "dataGridViewValues_Stat", "dataGridViewSeeds_IVRange", "dataGridView1", "dataGridView2"):
        text = set_grid_header_font(text, grid, family="Microsoft YaHei UI", size="9F")
    write_text(path, text)


def apply_dexivcheck_layout_fixes() -> None:
    path = ROOT / "RNGReporter/DexIVCheck.Designer.cs"
    text = read_text(path)
    text = replace_string_value(text, "label9", "Text", "\u7279\u60271")
    if "this.DGV.ColumnHeadersDefaultCellStyle.Font =" not in text:
        text = re.sub(
            r'(this\.DGV\.ColumnHeadersHeightSizeMode\s*=\s*System\.Windows\.Forms\.DataGridViewColumnHeadersHeightSizeMode\.AutoSize;\n)',
            r'\1            this.DGV.ColumnHeadersDefaultCellStyle.Font = new System.Drawing.Font("Microsoft YaHei UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));\n',
            text,
        )
    text = re.sub(
        r'(dataGridViewCellStyle1\.Font\s*=\s*)new System\.Drawing\.Font\("[^"]+", [^;]+;',
        r'\1new System.Drawing.Font("Microsoft YaHei UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));',
        text,
    )
    if 'this.Font = new System.Drawing.Font("Microsoft YaHei UI", 9F);' not in text:
        text = re.sub(
            r'(this\.AutoScaleMode = System\.Windows\.Forms\.AutoScaleMode\.Font;\n)',
            r'\1            this.Font = new System.Drawing.Font("Microsoft YaHei UI", 9F);\n',
            text,
        )
    write_text(path, text)


def apply_timefinder5th_runtime_fixes() -> None:
    path = ROOT / "RNGReporter/TimeFinder5th.cs"
    text = read_text(path)
    replacements = {
        'new ComboBoxItem("Ability 0", 0)': 'new ComboBoxItem("特性 0", 0)',
        'new ComboBoxItem("Ability 1", 1)': 'new ComboBoxItem("特性 1", 1)',
        'new ComboBoxItem("PID + IVs (Standard)", FrameType.Method5Standard)': 'new ComboBoxItem("PID + IVs（标准）", FrameType.Method5Standard)',
        'new ComboBoxItem("PID + IVs (Standard + C-Gear)", FrameType.Method5Natures)': 'new ComboBoxItem("PID + IVs（标准 + C-Gear）", FrameType.Method5Natures)',
        'new ComboBoxItem("IVs (C-Gear)", FrameType.Method5CGear)': 'new ComboBoxItem("IVs（C-Gear）", FrameType.Method5CGear)',
        'new ComboBoxItem("Tall Grass", EncounterType.Wild)': 'new ComboBoxItem("草丛", EncounterType.Wild)',
        'new ComboBoxItem("Dark Grass", EncounterType.WildDarkGrass)': 'new ComboBoxItem("深色草丛", EncounterType.WildDarkGrass)',
        'new ComboBoxItem("Swarm", EncounterType.WildSwarm)': 'new ComboBoxItem("大量出现", EncounterType.WildSwarm)',
        'new ComboBoxItem("Surfing", EncounterType.WildSurfing)': 'new ComboBoxItem("冲浪", EncounterType.WildSurfing)',
        'new ComboBoxItem("Fishing", EncounterType.WildSuperRod)': 'new ComboBoxItem("垂钓", EncounterType.WildSuperRod)',
        'new ComboBoxItem("Flying Shadow", EncounterType.WildShadow)': 'new ComboBoxItem("飞行影子", EncounterType.WildShadow)',
        'new ComboBoxItem("Stationary", EncounterType.Stationary)': 'new ComboBoxItem("定点宝可梦", EncounterType.Stationary)',
        'new ComboBoxItem("Roamer", EncounterType.Roamer)': 'new ComboBoxItem("游走宝可梦", EncounterType.Roamer)',
        'new ComboBoxItem("Larvesta/Happiny Egg", EncounterType.LarvestaHappiny)': 'new ComboBoxItem("燃烧虫/小福蛋的蛋", EncounterType.LarvestaHappiny)',
        'new ComboBoxItem("Jellicent", EncounterType.JellicentHA)': 'new ComboBoxItem("胖嘟嘟", EncounterType.JellicentHA)',
        'Filter = "第五世代神秘卡片 |*.pgf",': 'Filter = "第五世代神秘礼物 |*.pgf",',
        'Title = "选择神秘卡片文件"': 'Title = "选择神秘礼物文件"',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace(
        'if (comboBoxMethod.SelectedItem.ToString().Equals("PID + IVs (Standard + C-Gear)"))',
        'if (((ComboBoxItem)comboBoxMethod.SelectedItem).Reference.Equals(FrameType.Method5Natures))',
    )
    text = text.replace(
        'label9.Text = "IV filters are set for Entralink fast searching, but\\r\\n" +\n'
        '                                  "Min and Max Frames need to be between\\r\\n" +\n'
        '                                  "20 and 25.  (Setting both to 20 is recommended.)";',
        'label9.Text = "IV 筛选已适合连接森林快速搜索，但\\r\\n" +\n'
        '                                  "最小/最大帧需要在 20 到 25 之间。\\r\\n" +\n'
        '                                  "建议两者都设为 20。";',
    )
    text = text.replace(
        'label9.Text = "IV filters are set for fast searching, but\\r\\n" +\n'
        '                                  "Min and Max Frames need to be between\\r\\n" +\n'
        '                                  "0 and 5.  (Setting both to 0 is recommended.)";',
        'label9.Text = "IV 筛选已适合快速搜索，但\\r\\n" +\n'
        '                                  "最小/最大帧需要在 0 到 5 之间。\\r\\n" +\n'
        '                                  "建议两者都设为 0。";',
    )
    text = text.replace(
        'label9.Text += "\\r\\nOr 25 and 30 for Entralink abuse";',
        'label9.Text += "\\r\\n连接森林乱数可设为 25 到 30。";',
    )
    text = text.replace(
        'label9.Text = "IV filters are not set to allow fast searching.\\r\\nTry searching for a common spread" +\n'
        '                              "\\r\\nsuch as flawless, or a Trick Room spread.";',
        'label9.Text = "当前 IV 筛选不适合快速搜索。\\r\\n请尝试搜索较常见的分布，" +\n'
        '                              "\\r\\n例如 6V 或戏法空间分布。";',
    )
    write_text(path, text)


def apply_timefinder5th_designer_fixes() -> None:
    path = ROOT / "RNGReporter/TimeFinder5th.Designer.cs"
    text = read_text(path)
    text = text.replace("神秘卡片", "神秘礼物")
    text = text.replace('"Swarm"', '"大量出现"')
    text = replace_string_value(text, "label41", "Text", "3. 异色护符 / 记忆连接（仅 BW2）会影响命中帧，请一并计算。")
    text = re.sub(
        r'this\.label41\.Text\s*=\s*"3\. Shiny Charm / Memory Link .*?";',
        'this.label41.Text = "3. 异色护符 / 记忆连接（仅 BW2）会影响命中帧，请一并计算。";',
        text,
        flags=re.S,
    )
    for grid in ("dataGridViewCapValues", "dataGridViewEventResults", "dataGridViewPickup"):
        text = set_grid_header_font(text, grid, family="Microsoft YaHei UI", size="9F")
    write_text(path, text)


def apply_layout_fixes() -> None:
    apply_main_form_layout_fixes()
    apply_iv_filters_fixes()
    apply_language_defaults_fixes()
    apply_settings_designer_key_fixes()
    apply_seed_finder_fixes()
    apply_dexivcheck_layout_fixes()
    apply_timefinder3rd_layout_fixes()
    apply_timefinder3rd_runtime_fixes()
    apply_timefinder4th_layout_fixes()
    apply_timefinder4th_runtime_fixes()
    apply_timefinder5th_wording_fixes()
    apply_timefinder5th_runtime_fixes()
    apply_timefinder5th_designer_fixes()
    apply_encounter_string_fixes()


def normalize_changed_text_files() -> None:
    for path in changed_worktree_files():
        target_path = ROOT / path
        if target_path.exists() and Path(path).suffix in TEXT_FILE_SUFFIXES:
            write_text(target_path, read_text(target_path))


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

    apply_compile_safety_fixes()
    apply_source_identity_fixes()
    apply_layout_fixes()
    normalize_changed_text_files()
    current_review = build_current_review()
    write_review(current_review)
    print(f"applied entries: {len(review)}")
    print(f"review entries: {len(current_review)}")


if __name__ == "__main__":
    main()
