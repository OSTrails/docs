# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-06-29

### Added
- Live FAIR test catalogue in `docs/tools/toolbox/fair-tests.rst`: fetches all tests from the OSTrails Champion API (`https://tools.ostrails.eu/champion/tests/`), renders each as a collapsible card showing title, description, identifier, endpoint, and OpenAPI link, with a filter-as-you-type search box.

### Changed
- Toolbox section (`docs/tools/toolbox.rst`): updated title to "OSTrails DELIVERABLE 3.2: Toolbox of Testing Services"; revised introductory prose to clearly distinguish conceptual artefacts (Metrics, Benchmarks) from code-level artefacts (Tests, Algorithms) and explain the difference between DMP tests (code only) and FAIR tests (live endpoints).
- `docs/tools/toolbox/fair-metrics.rst`, `dmp-metrics.rst`, `dmp-tests.rst`: converted RST hyperlinks to raw HTML `<a>` tags so links open in a new tab.

## [0.1.0] - 2025-01-25

### Added
- Initial OSTrails documentation structure.