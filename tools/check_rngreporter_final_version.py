from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PROGRESS_FILE = ROOT / "RNGReporter" / "Progress.cs"
MAIN_FORM_FILE = ROOT / "RNGReporter" / "MainForm.cs"
FRAME_TYPE_FILE = ROOT / "RNGReporter" / "Objects" / "FrameType.cs"
MANAGER_FILES = [
    ROOT / "RNGReporter" / "TimeFinder3rd.cs",
    ROOT / "RNGReporter" / "TimeFinder4th.cs",
    ROOT / "RNGReporter" / "TimeFinder5th.cs",
    ROOT / "RNGReporter" / "EntralinkSeedSearch.cs",
    ROOT / "RNGReporter" / "Objects" / "Searchers" / "Searcher.cs",
    ROOT / "RNGReporter" / "DSIDWizard.cs",
    ROOT / "RNGReporter" / "UnovaLinkCalibration.cs",
]


def read(path):
    return path.read_text(encoding="utf-8-sig")


def main():
    failures = []
    main_form = read(MAIN_FORM_FILE)
    frame_type = read(FRAME_TYPE_FILE)
    progress_source = read(PROGRESS_FILE)

    if "Gen5Pickup" not in frame_type:
        failures.append("FrameType.Gen5Pickup is missing; this is not the Bambo-based final version.")
    if 'new ComboBoxItem("Pickup (Gen 5)", FrameType.Gen5Pickup)' not in main_form:
        failures.append("Main RNG method list is missing Pickup (Gen 5).")
    if "comboBoxMethod.SelectedIndex = 11;" not in main_form:
        failures.append("Main RNG method default is not Gen 5 PIDRNG.")

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
