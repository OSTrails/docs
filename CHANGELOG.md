# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.1] - 2026-07-23

### Changed

- `docs/tools/core-components.rst`: split the FAIR Tests and FAIR Algorithms live-catalogue widgets (each rendering close to 200 entries) back out into their own pages, `docs/tools/fair-tests.rst` and `docs/tools/fair-algorithms.rst`. Stacking both ~200-entry search widgets on one page made it unusable; `core-components.rst` now carries only a short description of each and a `:doc:` link out to the dedicated catalogue page, registered via a `:hidden:` toctree so the sidebar stays flat while the pages remain reachable and warning-free.

## [0.5.0] - 2026-07-23

### Changed

- `docs/tools/`: flattened the Toolbox navigation. `core-components.rst`, `testing-platforms.rst`, `registries.rst`, `supporting-tools.rst`, and `apis.rst` no longer embed nested `toctree`s pointing at wrapper pages; the wrapper pages' content (previously spread across `conceptual/`, `code/`, `assessment/`, `authoring-and-registering/`, `quality-control/`, and `apis/` subdirectories) is now inlined as sections on the five top-level pages themselves. Reviewers reported that reaching a tool's page took three or four clicks through single-entry sub-menus; every Toolbox page is now one click from `toolbox.rst`.
- `docs/tools/core-components.rst`: merged the FAIR Tests and FAIR Algorithms live-catalogue widgets onto one page; de-duplicated their shared CSS under `.catalog-*` classes and renamed their DOM ids (`fair-tests-*` / `fair-algorithms-*`) so both `<details>` search widgets can coexist without id collisions.
- Proofread and corrected grammar, spelling, and punctuation across all `docs/tools/` content (e.g. "may differs" → "may differ", "FAIROs" → "FAIROS", "controbuting" → "contributing", "leverated" → "leveraged", "eproducible" → "reproducible", "directy" → "directly", "the over FAIR score" → "the overall FAIR score", missing spaces after `**field**:` labels, and inconsistent heading capitalization).

### Fixed

- `docs/commons/fair/fair-test-results-vocabulary-ftr.rst`: updated the `FAIR assessment validation` link from a `:doc:` path into the now-removed `quality-control/ftr-validator` page to a `:ref:` targeting the `tool-ftr-validator` label on the merged `supporting-tools.rst` page.
- `docs/conf.py`: `release` was behind the changelog; bumped to match.

### Removed

- `docs/tools/conceptual/`, `docs/tools/code/`, `docs/tools/assessment/`, `docs/tools/authoring-and-registering/`, `docs/tools/quality-control/`, `docs/tools/apis/`, `docs/tools/fair.rst`, `docs/tools/dmp.rst`, `docs/tools/authoring.rst`, `docs/tools/quality-control.rst`: content merged into the five top-level Toolbox pages (see Changed); all `:ref:` labels these files defined (e.g. `tool-fair-champion`, `tool-foops`, `tool-fair-assessment-authoring-tool`, `tool-fair-tests`, `tool-ftr-validator`) were preserved on their new pages so existing cross-references keep resolving.

## [0.4.0] - 2026-07-02

### Merged

- Merged `upstream/next` into `Deliverable3-3`, resolving conflicts in favor of this branch's `tools/` restructuring (`conceptual/`, `code/`, `apis/` split) while incorporating upstream's RST fixes to the FAIR tutorials (missing blank lines after labels, proper `code-block` directives, non-colliding cross-reference labels, corrected `:doc:` targets).
- Resolved a rename/rename conflict on the OpenAIRE metadata validator page by keeping this branch's `quality-control/openaire-validator.rst` naming (disambiguates it from the newly added `ftr-validator.rst`).

### Fixed

- `docs/tools/toolbox.rst`: removed the stale `SKG Assesment Platforms <skg>` toctree entry (its three tools already live under the new `APIs` section) and fixed the `apis/openaire` target to `apis/openaire-graph`.
- `docs/tools/code/fair-tests.rst`: fixed a broken `:doc:` reference to the FAIR testing platforms page.
- `docs/commons/fair/fair-test-results-vocabulary-ftr.rst`: fixed a `:doc:` reference to `ftr-validator` that was resolving relative to the wrong directory.
- Removed duplicate hyperlink-target warnings in `find-test-for-digital-object.rst` and `register-benchmark.rst` by converting repeated same-text links to `:doc:` roles or anonymous hyperlinks.
- Fixed two "Title underline too short" warnings in `tools/code/fair-algorithms.rst` and `tools/conceptual/dmp-metrics.rst`.
- `docs/conf.py`: `release` was stuck at `0.2.0`, a version behind the CHANGELOG; bumped to match.

### Added

- `docs/tools/core-components.rst`, `testing-platforms.rst`, `registries.rst`, `supporting-tools.rst`, `apis.rst`: five new section pages so the Toolbox sidebar renders as a genuine multi-level hierarchy instead of a flat list. Sphinx only turns a toctree `:caption:` into a visible sidebar branch when it belongs to a page that is itself linked from a parent toctree — captions on toctrees nested purely inside another page's body are dropped during sidebar generation. `docs/tools/toolbox.rst` now links to these five pages instead of embedding their toctrees directly.
- `docs/tools/conceptual/metrics-and-benchmarks.rst` and `docs/tools/code/tests-and-algorithms.rst`: added missing page titles ("Conceptual Components" / "Code Components"). A toctree target with no title of its own doesn't get a sidebar node — Sphinx splices its children straight into the parent instead, which was silently flattening "Core Components" down to a single level.

### Changed

- `docs/tools/authoring.rst`: removed the duplicate `FAIR Validator` entry (already listed under `quality-control.rst`), fixing a "document referenced in multiple toctrees" ambiguity.
- `docs/tools/authoring-and-registering/ostrails-index.rst`: expanded the description to mention Champion's use of the index and clarify it's a machine-readable index, not user-facing.
- `docs/tools/conceptual/fair-benchmarks.rst`: fixed the FAIRassist registry search link, which was querying `recordType=metric_ids` instead of `recordType=benchmark_ids`.
- `docs/tools/conceptual/fair-metrics.rst`: capitalization fixes ("FAIR Assist" → "FAIRassist", "FAIRSharing" → "FAIRsharing").
- `docs/tools/quality-control/ftr-validator.rst`: retitled from "FAIR Assessment Record Validator" to "FAIR FTR Schema Validator" for clarity.

Docs build is now fully clean (`sphinx-build -E`: 0 warnings, 0 errors).

## [0.3.0] - 2026-07-02

### Merged

- Merged `upstream/next` into `Deliverable3-3`, resolving conflicts in favor of this branch's `tools/` restructuring (`conceptual/`, `code/`, `apis/` split) while incorporating upstream's RST fixes to the FAIR tutorials (missing blank lines after labels, proper `code-block` directives, non-colliding cross-reference labels, corrected `:doc:` targets).
- Resolved a rename/rename conflict on the OpenAIRE metadata validator page by keeping this branch's `quality-control/openaire-validator.rst` naming (disambiguates it from the newly added `ftr-validator.rst`).

### Fixed

- `docs/tools/toolbox.rst`: removed the stale `SKG Assesment Platforms <skg>` toctree entry (its three tools already live under the new `APIs` section) and fixed the `apis/openaire` target to `apis/openaire-graph`.
- `docs/tools/code/fair-tests.rst`: fixed a broken `:doc:` reference to the FAIR testing platforms page.
- `docs/commons/fair/fair-test-results-vocabulary-ftr.rst`: fixed a `:doc:` reference to `ftr-validator` that was resolving relative to the wrong directory.
- Removed duplicate hyperlink-target warnings in `find-test-for-digital-object.rst` and `register-benchmark.rst` by converting repeated same-text links to `:doc:` roles or anonymous hyperlinks.
- Fixed two "Title underline too short" warnings in `tools/code/fair-algorithms.rst` and `tools/conceptual/dmp-metrics.rst`.
- `docs/conf.py`: `release` was stuck at `0.2.0`, a version behind the CHANGELOG; bumped to match.

### Added

- `docs/tools/core-components.rst`, `testing-platforms.rst`, `registries.rst`, `supporting-tools.rst`, `apis.rst`: five new section pages so the Toolbox sidebar renders as a genuine multi-level hierarchy instead of a flat list. Sphinx only turns a toctree `:caption:` into a visible sidebar branch when it belongs to a page that is itself linked from a parent toctree — captions on toctrees nested purely inside another page's body are dropped during sidebar generation. `docs/tools/toolbox.rst` now links to these five pages instead of embedding their toctrees directly.
- `docs/tools/conceptual/metrics-and-benchmarks.rst` and `docs/tools/code/tests-and-algorithms.rst`: added missing page titles ("Conceptual Components" / "Code Components"). A toctree target with no title of its own doesn't get a sidebar node — Sphinx splices its children straight into the parent instead, which was silently flattening "Core Components" down to a single level.

### Changed

- `docs/tools/authoring.rst`: removed the duplicate `FAIR Validator` entry (already listed under `quality-control.rst`), fixing a "document referenced in multiple toctrees" ambiguity.
- `docs/tools/authoring-and-registering/ostrails-index.rst`: expanded the description to mention Champion's use of the index and clarify it's a machine-readable index, not user-facing.
- `docs/tools/conceptual/fair-benchmarks.rst`: fixed the FAIRassist registry search link, which was querying `recordType=metric_ids` instead of `recordType=benchmark_ids`.
- `docs/tools/conceptual/fair-metrics.rst`: capitalization fixes ("FAIR Assist" → "FAIRassist", "FAIRSharing" → "FAIRsharing").
- `docs/tools/quality-control/ftr-validator.rst`: retitled from "FAIR Assessment Record Validator" to "FAIR FTR Schema Validator" for clarity.

Docs build is now fully clean (`sphinx-build -E`: 0 warnings, 0 errors).

## 2026-06-30

### Added
- `docs/tools/toolbox/fair-algorithms.rst`: new page documenting the FAIR Algorithms artefact type.
- `docs/tools/toolbox/fair-benchmarks.rst`: new page documenting the FAIR Benchmarks artefact type.
- `docs/tools/authoring-and-registering/ostrails-index.rst`: OSTrails index page for the authoring-and-registering section.
- `docs/tools/authoring.rst`: top-level section page for authoring tools.
- `docs/tools/fair-assessment.rst`: top-level section page for FAIR assessment tools.
- `docs/tools/quality-control.rst`: top-level section page for quality-control tools.

### Changed
- Restructured the `docs/tools/` hierarchy: assessment tools (`fair-champion.rst`, `fairos.rst`, `foops.rst`, `rsfc.rst`) moved from `fair/` into `assessment/`; `fair-validator.rst` moved into `quality-control/`; authoring tools consolidated under `authoring-and-registering/`.
- `docs/tools/toolbox.rst`: updated to reflect the new deliverable-centric structure.
- `docs/index.rst`: updated top-level navigation to match the new hierarchy.

### Removed
- `docs/tools/toolbox/testing-platforms.rst`: content superseded by the new section pages.

## [0.2.0] - 2026-06-29

### Added
- Live FAIR test catalogue in `docs/tools/toolbox/fair-tests.rst`: fetches all tests from the OSTrails Champion API (`https://tools.ostrails.eu/champion/tests/`), renders each as a collapsible card showing title, description, identifier, endpoint, and OpenAPI link, with a filter-as-you-type search box.

### Changed
- Toolbox section (`docs/tools/toolbox.rst`): updated title to "OSTrails DELIVERABLE 3.2: Toolbox of Testing Services"; revised introductory prose to clearly distinguish conceptual artefacts (Metrics, Benchmarks) from code-level artefacts (Tests, Algorithms) and explain the difference between DMP tests (code only) and FAIR tests (live endpoints).
- `docs/tools/toolbox/fair-metrics.rst`, `dmp-metrics.rst`, `dmp-tests.rst`: converted RST hyperlinks to raw HTML `<a>` tags so links open in a new tab.

## [0.1.0] - 2025-01-25

### Added
- Initial OSTrails documentation structure.
