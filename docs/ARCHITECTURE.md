# Technical Architecture — Climate Radar

## Overview

Climate Radar is a **single-file React application** compiled via Babel standalone in the browser. This design choice prioritizes portability and zero-dependency deployment over build complexity.

---

## Component Map

```
App (root)
├── Radar (Canvas)
│   ├── alertsToBlips()         — maps filtered alerts → radar positions
│   ├── Golden-angle spread     — prevents blip clustering
│   └── Risk-radius mapping     — High=inner, Medium=mid, Low=outer
│
├── Header
│   └── Live indicator + timestamp
│
├── Left Column
│   ├── ThreatMatrix            — High/Medium/Low counts
│   └── NarrativeShiftIndex     — trend bars
│
├── Center Column (Radar Hero)
│   ├── RadarCanvas (340px)
│   ├── Signal counter          — updates with filter
│   ├── Sources scanned         — increments per scan
│   └── RUN NEW SCAN button
│
└── Right Column
    ├── SearchBar               — cross-tab fuzzy search
    ├── RecencyToggle           — ALL TIME / RECENT (≤90 days)
    ├── CategoryChips           — filter by signal type
    ├── PDF Export button       — jsPDF, full report
    ├── KeywordWatchBar         — add/remove keywords, scan
    └── Tabs
        ├── Intelligence Feed   — alert cards with freshness badges
        ├── Keyword Results     — filtered by watched keywords
        └── Strategic Brief     — pre-written analysis sections
```

---

## State Architecture

| State | Type | Purpose |
|---|---|---|
| `alerts` | Array | Current sorted alert list |
| `filter` | String | Active category filter |
| `search` | String | Cross-tab search query |
| `sel` | Object | Currently selected alert |
| `scanning` | Boolean | Scan animation active |
| `keywords` | Array | Active keyword watchlist |
| `kwResults` | Array | Keyword scan matches |
| `linkStatus` | Object | Per-alert link verification state |
| `recentOnly` | Boolean | ≤90-day filter active |
| `sourcesScanned` | Number | Increments per scan run |
| `scanCount` | Number | Total scans this session |

---

## Date System

All signal dates are computed dynamically using `daysAgo(n)`:

```javascript
const daysAgo = (n) => {
  const d = new Date();
  d.setDate(d.getDate() - n);
  return d.toISOString().slice(0, 10);
};
```

This ensures dates always reflect the current session date — opening the app tomorrow will show tomorrow's date on the most recent signals.

---

## Link Verification

Uses `fetch()` with `mode: 'no-cors'` and a 7-second `AbortController` timeout:

- **ok** — Domain resolved (opaque response received)
- **fail** — Network error / domain unreachable
- **timeout** — No response within 7 seconds
- **checking** — Request in flight

Note: `no-cors` mode returns opaque responses — domain reachability is confirmed but HTTP status code is not accessible. Page-level 404s cannot be distinguished from 200s via this method.

---

## PDF Generation

Uses **jsPDF 2.5.1** loaded from cdnjs. The export:

1. Renders a dark header block with title and metadata
2. Iterates all currently filtered alerts
3. Color-codes each row by risk level (RGB backgrounds)
4. Embeds clickable hyperlinks via `textWithLink()`
5. Adds a red bold footer with classification marking

Arabic text is intentionally excluded from PDF output — jsPDF's built-in fonts do not support RTL/Arabic rendering and produce garbled output.

---

## Security Model

| Layer | Implementation |
|---|---|
| Access control | SHA-256 PIN hash checked client-side |
| Session persistence | `sessionStorage` — cleared on tab close |
| DevTools deterrence | `keydown` event suppression (F12, Ctrl+Shift+I/J/C, Ctrl+U) |
| Right-click | `contextmenu` event prevented |
| Print watermark | `document.title` overridden on `beforeprint` |

> **Note:** Client-side security provides deterrence, not cryptographic guarantees. For true data security, host on an authenticated private server.
