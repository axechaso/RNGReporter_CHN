from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PROGRESS_FILE = ROOT / "RNGReporter" / "Progress.cs"
MAIN_FORM_FILE = ROOT / "RNGReporter" / "MainForm.cs"
MAIN_FORM_DESIGNER_FILE = ROOT / "RNGReporter" / "MainForm.Designer.cs"
FRAME_TYPE_FILE = ROOT / "RNGReporter" / "Objects" / "FrameType.cs"
FRAME_FILE = ROOT / "RNGReporter" / "Objects" / "Frame.cs"
FUNCTIONS_FILE = ROOT / "RNGReporter" / "Objects" / "Functions.cs"
LANGUAGE_FILE = ROOT / "RNGReporter" / "Objects" / "Language.cs"
SEED_FINDER_DESIGNER_FILE = ROOT / "RNGReporter" / "SeedFinder.Designer.cs"
TIME_FINDER4_FILE = ROOT / "RNGReporter" / "TimeFinder4th.cs"
TIME_FINDER4_DESIGNER_FILE = ROOT / "RNGReporter" / "TimeFinder4th.Designer.cs"
TIME_FINDER5_FILE = ROOT / "RNGReporter" / "TimeFinder5th.cs"
TIME_FINDER5_DESIGNER_FILE = ROOT / "RNGReporter" / "TimeFinder5th.Designer.cs"
SEARCH_ELM_FILE = ROOT / "RNGReporter" / "SearchElm.cs"
SEARCH_ELM_DESIGNER_FILE = ROOT / "RNGReporter" / "SearchElm.Designer.cs"
SEARCH_ELM_V_FILE = ROOT / "RNGReporter" / "SearchElmV.cs"
SEARCH_ELM_V_DESIGNER_FILE = ROOT / "RNGReporter" / "SearchElmV.Designer.cs"
MANAGER_FILES = [
    ROOT / "RNGReporter" / "TimeFinder3rd.cs",
    TIME_FINDER4_FILE,
    TIME_FINDER5_FILE,
    ROOT / "RNGReporter" / "EntralinkSeedSearch.cs",
    ROOT / "RNGReporter" / "Objects" / "Searchers" / "Searcher.cs",
    ROOT / "RNGReporter" / "DSIDWizard.cs",
    ROOT / "RNGReporter" / "UnovaLinkCalibration.cs",
]


def read(path):
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "gb18030"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            pass
    return data.decode("utf-8-sig", errors="replace")


def main():
    failures = []
    main_form = read(MAIN_FORM_FILE)
    main_designer = read(MAIN_FORM_DESIGNER_FILE)
    frame_type = read(FRAME_TYPE_FILE)
    frame_source = read(FRAME_FILE)
    functions_source = read(FUNCTIONS_FILE)
    language_source = read(LANGUAGE_FILE)
    seed_finder_designer = read(SEED_FINDER_DESIGNER_FILE)
    time_finder4 = read(TIME_FINDER4_FILE)
    time_finder4_designer = read(TIME_FINDER4_DESIGNER_FILE)
    time_finder5 = read(TIME_FINDER5_FILE)
    time_finder5_designer = read(TIME_FINDER5_DESIGNER_FILE)
    search_elm = read(SEARCH_ELM_FILE)
    search_elm_designer = read(SEARCH_ELM_DESIGNER_FILE)
    search_elm_v = read(SEARCH_ELM_V_FILE)
    search_elm_v_designer = read(SEARCH_ELM_V_DESIGNER_FILE)
    progress_source = read(PROGRESS_FILE)

    if "Gen5Pickup" not in frame_type:
        failures.append("FrameType.Gen5Pickup is missing; this is not the Bambo-based final version.")
    if 'new ComboBoxItem("Pickup (Gen 5)", FrameType.Gen5Pickup)' not in main_form:
        failures.append("Main RNG method list is missing Pickup (Gen 5).")
    if "comboBoxMethod.SelectedIndex = 11;" not in main_form:
        failures.append("Main RNG method default is not Gen 5 PIDRNG.")

    if '"Swarm"});' in main_designer:
        failures.append("Main encounter-slot dropdown still shows raw Swarm.")
    if '"大量出现"});' not in main_designer:
        failures.append("Main encounter-slot dropdown is missing 大量出现.")
    encounter_chs = language_source.split("public static readonly string[] encounterItemsCHS =", 1)[-1][:180]
    if '"大量出现"' not in encounter_chs:
        failures.append("Chinese encounter item 0 should be 大量出现, not the Swarm ability name.")
    if '"虫之预感"' not in language_source.split("public static readonly string[] abilityNameCHS =", 1)[-1]:
        failures.append("Ability Swarm translation should remain 虫之预感.")

    if "Encounter slots are used to determine" in main_form + time_finder4 + time_finder5:
        failures.append("Encounter-slot tooltip is still untranslated.")
    if "遭遇槽用于决定野生对战中出现的宝可梦" not in main_form:
        failures.append("Main encounter-slot tooltip is missing the Chinese text.")
    if "Trigger at 20th step" in frame_source:
        failures.append("20-step encounter trigger table text is still English.")
    if "Occidentary" in main_form + main_designer + read(ROOT / "RNGReporter" / "TimeFinder3rd.Designer.cs"):
        failures.append("Offset column header still contains the old Occidentary text.")
    if "A bolded nature indicates" in main_form + time_finder4 + time_finder5:
        failures.append("Nature tooltip is still partly untranslated.")
    main_grid_bindings = {
        "Offset": "Offset",
        "Time": "Time",
        "Elm": "Elm",
        "Ratio": "Ratio",
        "Level": "Level",
        "Ability": "Ability",
        "Coin": "Coin",
        "Characteristic": "Characteristic",
        "Synchable": "Synchable",
    }
    for column, property_name in main_grid_bindings.items():
        expected_binding = f'this.{column}.DataPropertyName = "{property_name}";'
        if expected_binding not in main_designer:
            failures.append(f"Main grid column {column} is not bound to Frame.{property_name}.")
    localized_time_binding = 'Time.DataPropertyName = "' + chr(0x65F6) + chr(0x95F4) + '";'
    if localized_time_binding in main_form:
        failures.append("MainForm still resets the Time column binding to a localized name.")

    if 'new ComboBoxItem("算法 J", FrameType.MethodJ)' in time_finder4:
        failures.append("TimeFinder4th Method J label should keep Method untranslated.")
    if 'new ComboBoxItem("Method J", FrameType.MethodJ)' not in time_finder4:
        failures.append("TimeFinder4th Method J label is missing.")
    if 'new ComboBoxItem("Method K", FrameType.MethodK)' not in time_finder4:
        failures.append("TimeFinder4th Method K label is missing.")

    if '"拉帝欧斯\\\\拉迪亚斯"' in seed_finder_designer:
        failures.append("SeedFinder keypress dropdown still translates L as Latios/Latias.")
    button_strings = functions_source.split("public static readonly string[] buttonStrings", 1)[-1][:500]
    if '"R"' not in button_strings or '"L"' not in button_strings:
        failures.append("Button display strings should keep R/L untranslated.")

    data_error_targets = {
        "MainForm.Designer.cs": main_designer,
        "TimeFinder4th.Designer.cs": time_finder4_designer,
        "TimeFinder5th.Designer.cs": time_finder5_designer,
    }
    for name, source in data_error_targets.items():
        if ".DataError +=" not in source:
            failures.append(f"{name} does not wire DataGridView DataError handling.")
    if "dataGridViewValues_DataError" not in main_form:
        failures.append("MainForm is missing DataGridView DataError handling.")
    if "dataGridViewValues.DataSource = null;" not in main_form:
        failures.append("Main grid should clear its old data source before rebinding.")

    if 'AddLetter("炎帝")' in search_elm or 'this.buttonE.Text = "炎帝";' in search_elm_designer:
        failures.append("SearchElm should use E for Elm calls, not the Entei name.")
    if 'Text = "炎帝";' in search_elm_v_designer:
        failures.append("SearchElmV should use E buttons, not the Entei name.")
    if "ElmCallText" not in search_elm or "ElmCallText" not in search_elm_v:
        failures.append("Elm call help text should be shared between single and multi search windows.")
    for marker in ("中：", "日：", "英：", "カントー地方", "Pokérus"):
        if marker not in search_elm:
            failures.append(f"Elm call help text is missing multilingual marker: {marker}")

    if 'throw new Exception("操作被取消")' in progress_source:
        failures.append("Progress cancellation still throws a generic localized Exception.")
    if "throw new OperationCanceledException" not in progress_source:
        failures.append("Progress cancellation does not throw OperationCanceledException.")

    for path in MANAGER_FILES:
        source = read(path)
        if 'exception.Message != "Operation Cancelled"' in source:
            failures.append(f"{path.relative_to(ROOT)} still detects cancellation by English message.")
        if "catch (OperationCanceledException)" not in source:
            failures.append(f"{path.relative_to(ROOT)} does not catch OperationCanceledException.")

    sortable_managers = MANAGER_FILES[:5]
    for path in sortable_managers:
        source = read(path)
        if "gridSorter" in source and "if (!cancelled)" not in source:
            failures.append(f"{path.relative_to(ROOT)} can still sort large result grids after cancellation.")

    if failures:
        raise SystemExit("\n".join(failures))

    print("final version checks passed")


if __name__ == "__main__":
    main()
