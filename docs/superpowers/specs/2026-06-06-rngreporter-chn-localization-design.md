# RNGReporter Chinese Localization Migration Design

## Goal

Port the existing Chinese localization from `axechaso/RNGReporter_CHN` onto `Bambo-Rambo/RNGReporter` while preserving the newer upstream fixes and features. Translate newly added or still-English UI text and generate a review list so the user can校对 the Chinese copy before final publication.

## Source And Target

- Reference localization: `C:\Users\axenx\Documents\rngreporter`
- Target codebase: `C:\Users\axenx\AppData\Local\Temp\codex-rngreporter-bambo`
- Target upstream: `Bambo-Rambo/RNGReporter`, branch `master`, currently at `v10.3.4`
- Reference fork: `axechaso/RNGReporter_CHN`, branch `master`

The histories diverged at commit `2c77b8e`. The target has many newer bug fixes and added forms, so a direct merge is too conflict-heavy and risks losing upstream behavior.

## Scope

Migrate Chinese text for existing windows and shared objects from the CHN reference into the target repository. Cover visible WinForms text in `.Designer.cs`, `.resx`, and code-driven strings in `.cs` files when those strings affect menus, labels, buttons, grid columns, combo boxes, dialogs, warnings, and user-facing output.

Translate new or still-English target-only areas, including:

- `Gen5FrameFinder`
- `CgearCalibrator`
- `TimeFinder5thPickup`
- target-only additions in Gen 5 TimeFinder, GameCube, Profile Editor, Researcher, and related helper classes

Do not redesign localization architecture in this pass. Keep the existing project structure and avoid introducing a new resource-loading system unless the current code already uses it for the specific string.

## Translation Rules

Reuse the CHN reference wording where the same source text or UI role exists. Keep established RNG terms and abbreviations stable, including `PID`, `SID`, `TID`, `IV`, `Seed`, `Frame`, `Method`, and game generation labels when translating them would reduce clarity for the existing audience.

For Pokemon-specific names, use 52Poke / 神奇宝贝百科 terminology as the reference. This includes Pokemon species, moves, abilities, items, locations, and named in-game systems such as `C-Gear`, `Entralink`, and `Pass Power`.

For new translations, prefer concise Chinese UI text that fits the existing WinForms layout. When a long English label becomes too wide in Chinese, adjust only the local control size or text wrapping needed to prevent clipping. Do not change calculations or event logic for translation-only edits.

## Implementation Shape

Use the target repository as the edited tree and the CHN repository as a read-only reference. Build a translation map from matching files where possible, then apply translations file by file:

1. Match same-name forms and shared classes between the reference and target.
2. Transfer equivalent translated user-facing strings while preserving target logic.
3. Inspect target-only files for remaining English UI text and translate them.
4. Generate `translation-review.md` with entries containing source file, line or key, original English, and proposed Chinese.
5. Run conflict, encoding, and leftover-English scans.

## Verification

Run `git status` and scans for conflict markers and encoding problems. Attempt `dotnet build RNGReporter.sln` if the local .NET Framework 4.8 reference assemblies are available. If the build cannot run because the targeting pack is missing, report that explicitly and provide the static verification results instead.

## Deliverables

- Modified Bambo-Rambo target tree with Chinese localization applied.
- A review file for user校对 of newly translated or uncertain text.
- A concise summary of remaining English text that was intentionally left unchanged or needs manual confirmation.
