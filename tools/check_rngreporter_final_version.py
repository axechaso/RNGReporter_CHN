import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PROGRESS_FILE = ROOT / "RNGReporter" / "Progress.cs"
PROGRAM_FILE = ROOT / "RNGReporter" / "Program.cs"
GLOBAL_UI_FONT_FILE = ROOT / "RNGReporter" / "GlobalUiFont.cs"
MAIN_FORM_FILE = ROOT / "RNGReporter" / "MainForm.cs"
MAIN_FORM_DESIGNER_FILE = ROOT / "RNGReporter" / "MainForm.Designer.cs"
IV_FILTERS_DESIGNER_FILE = ROOT / "RNGReporter" / "Controls" / "IVFilters.Designer.cs"
ADJACENTS_FILE = ROOT / "RNGReporter" / "Adjacents.cs"
FRAME_TYPE_FILE = ROOT / "RNGReporter" / "Objects" / "FrameType.cs"
FRAME_FILE = ROOT / "RNGReporter" / "Objects" / "Frame.cs"
FUNCTIONS_FILE = ROOT / "RNGReporter" / "Objects" / "Functions.cs"
LANGUAGE_FILE = ROOT / "RNGReporter" / "Objects" / "Language.cs"
SEED_FINDER_DESIGNER_FILE = ROOT / "RNGReporter" / "SeedFinder.Designer.cs"
UNOVA_LINK_DESIGNER_FILE = ROOT / "RNGReporter" / "UnovaLinkCalibration.Designer.cs"
TIME_FINDER3_DESIGNER_FILE = ROOT / "RNGReporter" / "TimeFinder3rd.Designer.cs"
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
    program_source = read(PROGRAM_FILE)
    global_ui_font = read(GLOBAL_UI_FONT_FILE)
    main_form = read(MAIN_FORM_FILE)
    main_designer = read(MAIN_FORM_DESIGNER_FILE)
    iv_filters_designer = read(IV_FILTERS_DESIGNER_FILE)
    adjacents_source = read(ADJACENTS_FILE)
    frame_type = read(FRAME_TYPE_FILE)
    frame_source = read(FRAME_FILE)
    functions_source = read(FUNCTIONS_FILE)
    language_source = read(LANGUAGE_FILE)
    seed_finder_designer = read(SEED_FINDER_DESIGNER_FILE)
    unova_link_designer = read(UNOVA_LINK_DESIGNER_FILE)
    time_finder3_designer = read(TIME_FINDER3_DESIGNER_FILE)
    time_finder4 = read(TIME_FINDER4_FILE)
    time_finder4_designer = read(TIME_FINDER4_DESIGNER_FILE)
    time_finder5 = read(TIME_FINDER5_FILE)
    time_finder5_designer = read(TIME_FINDER5_DESIGNER_FILE)
    search_elm = read(SEARCH_ELM_FILE)
    search_elm_designer = read(SEARCH_ELM_DESIGNER_FILE)
    search_elm_v = read(SEARCH_ELM_V_FILE)
    search_elm_v_designer = read(SEARCH_ELM_V_DESIGNER_FILE)
    progress_source = read(PROGRESS_FILE)

    binding_pattern = re.compile(r'this\.(\w+)\.DataPropertyName = "([^"]*)";')
    for path in (ROOT / "RNGReporter").rglob("*.Designer.cs"):
        for match in binding_pattern.finditer(read(path)):
            property_name = match.group(2)
            if any(ord(character) > 127 for character in property_name):
                failures.append(
                    f"{path.relative_to(ROOT)} column {match.group(1)} has localized DataPropertyName {property_name!r}."
                )
    if "GlobalUiFont.Install();" not in program_source:
        failures.append("Program should install the global UI font hook before opening forms.")
    if 'FontFamilyName = "Microsoft YaHei UI"' not in global_ui_font:
        failures.append("Global UI font should use Microsoft YaHei UI.")
    if "ApplyToolStripFont" not in global_ui_font or "ApplyGridFont" not in global_ui_font:
        failures.append("Global UI font should cover menus/toolstrips and data grids.")
    if "this.MinimumSize = new System.Drawing.Size(365, 166);" not in iv_filters_designer:
        failures.append("IVFilters should keep a 365px minimum width for the global UI font.")
    if "this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Inherit;" not in iv_filters_designer:
        failures.append("IVFilters should inherit host DPI scaling so the Speed row is not clipped after the global font change.")
    if "new System.Drawing.Size(315, 166)" in (
        main_designer + iv_filters_designer + time_finder3_designer + time_finder4_designer + time_finder5_designer
    ):
        failures.append("An IVFilters host still uses the old 315px width.")

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
    if "Occidentary" in main_form + main_designer + time_finder3_designer:
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
    if 'this.Text = "GEN4 Seed查找/计算";' not in seed_finder_designer:
        failures.append("SeedFinder title should be readable Chinese, not mojibake.")
    if any(marker in seed_finder_designer for marker in ("�", "锟", "����")):
        failures.append("SeedFinder designer still contains mojibake markers.")
    if "4th Gen Seed Finder / Generator" in seed_finder_designer:
        failures.append("SeedFinder title regressed to English.")
    if "If you are looking for your initial seed" in seed_finder_designer:
        failures.append("SeedFinder initial-seed help text is still English.")
    if '"Black",' in seed_finder_designer or '"White",' in seed_finder_designer:
        failures.append("SeedFinder version dropdown should use Chinese game names.")
    if 'this.gbSpins.Location = new System.Drawing.Point(434, 11);' not in unova_link_designer:
        failures.append("Unova Link calibration should keep the direction sequence panel in the horizontal layout.")
    if 'this.ClientSize = new System.Drawing.Size(860, 520);' not in unova_link_designer:
        failures.append("Unova Link calibration should keep the wider horizontal window.")
    if 'this.dgvResults.Size = new System.Drawing.Size(860, 220);' not in unova_link_designer:
        failures.append("Unova Link calibration results grid should be below the horizontal panels.")
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
    if "e.Value == null" not in adjacents_source:
        failures.append("Adjacent seed grid formatting should ignore empty cell values instead of throwing.")

    if 'AddLetter("炎帝")' in search_elm or 'this.buttonE.Text = "炎帝";' in search_elm_designer:
        failures.append("SearchElm should use E for Elm calls, not the Entei name.")
    if 'Text = "炎帝";' in search_elm_v_designer:
        failures.append("SearchElmV should use E buttons, not the Entei name.")
    if "this.buttonOk.Anchor = System.Windows.Forms.AnchorStyles.Bottom;" in search_elm_designer:
        failures.append("SearchElm OK button should not use Bottom anchor; dynamic height pushes it out of view.")
    if "this.buttonCancel.Anchor = System.Windows.Forms.AnchorStyles.Bottom;" in search_elm_designer:
        failures.append("SearchElm Cancel button should not use Bottom anchor; dynamic height pushes it out of view.")
    if "this.buttonOk.Anchor = System.Windows.Forms.AnchorStyles.Bottom;" in search_elm_v_designer:
        failures.append("SearchElmV OK button should not use Bottom anchor; dynamic height pushes it out of view.")
    if "this.buttonCancel.Anchor = System.Windows.Forms.AnchorStyles.Bottom;" in search_elm_v_designer:
        failures.append("SearchElmV Cancel button should not use Bottom anchor; dynamic height pushes it out of view.")
    elm_label = "".join(chr(c) for c in [0x7A7A, 0x6728, 0x535A, 0x58EB, 0x20, 0x2F, 0x20, 0x30A6, 0x30C4, 0x30AE, 0x535A, 0x58EB, 0x20, 0x2F, 0x20, 0x45, 0x6C, 0x6D])
    irwin_label = "".join(chr(c) for c in [0x9EA6, 0x514B, 0x20, 0x2F, 0x20, 0x30DE, 0x30A4, 0x30AF, 0x20, 0x2F, 0x20, 0x49, 0x72, 0x77, 0x69, 0x6E])
    if elm_label not in search_elm_designer:
        failures.append("SearchElm Elm radio label should show Chinese/Japanese/English names.")
    if irwin_label not in search_elm_designer:
        failures.append("SearchElm Irwin radio label should show Chinese/Japanese/English names.")
    if "ElmCallText" not in search_elm or "ElmCallText" not in search_elm_v:
        failures.append("Elm call help text should be shared between single and multi search windows.")
    if "buttonLanguage" not in search_elm or "buttonLanguage" not in search_elm_v:
        failures.append("Elm phone help text should have a language switch button in both search windows.")
    if search_elm.count("PhoneHelpLanguage.Japanese") < 1 or search_elm_v.count("PhoneHelpLanguage.Japanese") < 1:
        failures.append("Elm phone help text should default to Japanese in both search windows.")
    if "NextLanguage" not in search_elm or "NextLanguage" not in search_elm_v:
        failures.append("Elm phone help language button should cycle through languages.")
    inline_multilingual_markers = [
        chr(0x4E2D) + chr(0xFF1A),
        chr(0x65E5) + chr(0xFF1A),
        chr(0x82F1) + chr(0xFF1A),
    ]
    for marker in inline_multilingual_markers:
        if marker in search_elm:
            failures.append("Elm phone help text should show one selected language at a time, not inline trilingual text.")

    expected_japanese_phone_text = [
        "げんきかい？",
        "きみの かつやくを きいて",
        "でんわ うれしいなあ！",
        "カントーには まだ ぼくの しらない ポケモンが いるだろうし、",
        "ポケモンの しんかというのは ほんとうに おくが ふかいよねぇ！",
        "ポケルスが くっついた ポケモンは どうやら そだちが よくなる みたい",
    ]
    for text in expected_japanese_phone_text:
        if text not in search_elm:
            failures.append(f"Elm phone Japanese text is missing: {text}")

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
