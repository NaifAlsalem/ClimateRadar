# Technical Architecture

## Overview

Climate Radar is built as a single HTML file. There is no build process, no package manager, no server to configure - just open the file in a browser, enter the access PIN, and you are looking at live climate intelligence within seconds.
React and Babel, two lightweight JavaScript libraries, handle everything that updates in real time. Both load silently when you open the file, with nothing to install and nothing to configure.
This was a deliberate architectural choice. 

A tool that requires a developer to set up is a tool that does not get used during a negotiation session. By keeping everything inside a single file, any team member can open it on any laptop, in any location, without depending on IT support or a dedicated server. The file is also easy to version, share securely, and update without breaking anything.

The tradeoff is that this is client-side software, not a hardened system. It is built for operational speed and accessibility. When the use case evolves to require multi-user access, persistent storage, or tighter security controls, the architecture can grow with it.

---

## Component Map
The interface is made up of four main parts that work together. The tree below shows how they relate to each other under the hood.

```
App (root)
├── Radar (Canvas)
│   ├── alertsToBlips()         - maps filtered alerts to radar positions
│   ├── Golden-angle spread     - prevents blip clustering
│   └── Risk-radius mapping     - High=inner, Medium=mid, Low=outer
│
├── Header
│   └── Live indicator + timestamp
│
├── Left Column
│   ├── ThreatMatrix            - High/Medium/Low counts
│   └── NarrativeShiftIndex     - trend bars
│
├── Center Column (Radar Hero)
│   ├── RadarCanvas (340px)
│   ├── Signal counter          - updates with filter
│   ├── Sources scanned         - increments per scan
│   └── RUN NEW SCAN button
│
└── Right Column
    ├── SearchBar               - cross-tab fuzzy search
    ├── RecencyToggle           - ALL TIME / RECENT (30 days)
    ├── CategoryChips           - filter by signal type
    ├── PDF Export button       - jsPDF, full report
    ├── KeywordWatchBar         - add/remove keywords, scan
    └── Tabs
        ├── Intelligence Feed   - alert cards with freshness badges
        ├── Keyword Results     - filtered by watched keywords
        └── Strategic Brief     - structured analysis with live signal references
```

---

## State Architecture
Everything the app tracks at any given moment is listed below. Each variable updates instantly as you interact with the interface.


| State | Type | Purpose |
|---|---|---|
| `alerts` | Array | The live list of signals, sorted by risk |
| `filter` | String | Which category chip is active |
| `search` | String | The text query filtering across all tabs |
| `sel` | Object | Whichever signal card is currently open |
| `scanning` | Boolean | Whether a scan is in progress |
| `keywords` | Array | The current active keyword watchlist |
| `kwResults` | Array | What came back from your last keyword scan |
| `linkStatus` | Object | Whether each signal's source URL is reachable |
| `recentOnly` | Boolean | Whether the 30-day recency filter is on |
| `sourcesScanned` | Number | Running total of items fetched across scans |
| `scanCount` | Number | How many scans you have run this session |

---

## Date System

Signal dates are always calculated relative to the day you open the file, not hardcoded to a fixed calendar date. This means the freshness badges (TODAY, NEW, Xd AGO) stay accurate no matter when the file was last edited or shared.
The function takes a number, counts that many days back from today, and returns the result as a date string.

```javascript
const daysAgo = (n) => {
  const d = new Date();
  d.setDate(d.getDate() - n);
  return d.toISOString().slice(0, 10);
};
```

---

## Link Verification
When you open a signal card, the app automatically fires a request to that signal's source URL to check whether it is reachable. The result appears as one of four states:

Uses `fetch()` with `mode: 'no-cors'` and a 7-second `AbortController` timeout:

- **VERIFIED** — the domain responded and the link appears to be live
- **UNREACHABLE** —  the domain could not be reached at all
- **TIMED OUT** — no response came back within 7 seconds
- **CHECKING** — the request is currently in flight

**Note:** There is one limitation here. Due to how browsers handle cross-origin requests, the check runs in `no-cors` mode. This means the app can confirm that a domain is reachable, but it cannot read the actual response code. If you are unsure, click through to the source directly.

---

## PDF Generation

Uses **jsPDF 2.5.1** loaded from cdnjs. The export:

The PDF export is handled entirely in the browser using **jsPDF 2.5.1**, a lightweight library that builds documents on the fly without sending anything to a server. When you hit the PDF button, it takes whatever signals are currently visible on screen - respecting your active filters and search - and compiles them into a formatted report.
The output includes a header with the report title and generation timestamp, each signal color-coded by risk level, clickable source links, and the classified footer at the bottom.

**Important Note**: Arabic text is not included in the PDF. The library's built-in fonts do not support right-to-left rendering, and forcing it produces unreadable output. The English-only version exports cleanly. This will be revisited later as we roll newer versions. 

---

## Security Model

| Layer | Implementation |
|---|---|
| Access control | The PIN is never stored in plain text. It is converted to a SHA-256 hash and checked against the stored hash on entry |
| Session persistence | The unlocked session lives in `sessionStorage` , which clears automatically when you close the tab |
| DevTools deterrence | Common keyboard shortcuts used to inspect code are blocked (F12, Ctrl+Shift+I, Ctrl+U) |
| Right-click | Disabled to prevent easy access to page source |
| Print watermark | `document.title` overridden on `beforeprint` |

> **Note:** This is client-side protection, not a security perimeter. It covers casual access and discourages casual inspection. Anyone with serious technical intent can work around it. If the tool ever moves to a wider audience or handles more sensitive material, the right next step is adding server-side authentication.
