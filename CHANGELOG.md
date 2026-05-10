# Changelog

All notable changes to Climate Radar are documented here.
- Note: Please contact: Naif Alsalem, for any contribution on GitHub. 

---

## [2.1.0] — 2026-05-06

### Added
- Dynamic date system where all signal dates now calculated relative to today using `daysAgo(n)` helper.
- Sources Scanned counter increments with each RUN NEW SCAN (+12 to +50 per run).
- Scan run counter displayed below radar.
- RECENT ONLY toggle (≤90-day filter) with  indicator.

### Changed
- PDF footer line now bold red with red separator line above
- Methane signal updated to COP30 2025 UNEP/GMP Ministerial source (Nov 2025)
- All signal links updated to specific deep-link pages

### Fixed
- Search bar now works across all tabs including Keyword Results
- Search auto-switches from Strategic Brief tab to Intelligence Feed on keystroke
- ✕ clear button added to search input
- Arabic text removed from PDF (jsPDF rendering incompatibility)

---

## [2.0.0] — 2026-04-15

### Added
- PIN authentication with SHA-256 hashing and session persistence
- Anti-theft measures: right-click disabled, DevTools shortcuts blocked
- Link verification system (HEAD check with 7s timeout + RE-CHECK button)
- `linkLabel` and `linkNote` fields (specific source page and section references)
- Freshness badge system: NEW / RECENT / Xd AGO / STALE
- Three-column layout with radar as centered hero element
- Risk legend below radar

### Changed
- Radar moved to center column with 340px canvas and radial background glow
- Left column: Threat Matrix + Narrative Shift Index
- Right column: full intelligence feed

---

## [1.5.0] — 2026-03-03

### Added
- Keyword Watch bar with persistent keyword chips
- KEYWORD RESULTS tab with matched keyword highlighting
- `filteredKw` state for search-within-keyword-results

### Changed
- Radar blips now reflect filtered alert list (golden-angle spread)
- Radar signal count label updates dynamically with filter

---

## [1.0.0] — 2026-02-01

### Initial Release
- Live radar canvas with animated sweep
- Intelligence Feed with 10 climate signals
- Threat Matrix, Narrative Shift Index
- RUN NEW SCAN button with animated messages
- PDF export via jsPDF
- Category filter chips, search bar
- Strategic Brief tab
- Signal Detail panel with source link
