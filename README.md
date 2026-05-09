# Climate Radar: A Strategic Intelligence Platform

> **Private Repository** · Authorized access only · Dr. Naif Alsalem

---

## Overview

**Climate Radar** is a browser-based strategic intelligence dashboard purpose-built for monitoring, analyzing, and reporting on global climate negotiation signals in real time. It surfaces risks, narrative shifts, and coalition opportunities relevant to Arab Group and Saudi negotiating positions across major international climate bodies.

The platform requires no server, no installation, and no build step as it runs entirely as a single self-contained HTML file with PIN-protected access.
<img width="1913" height="854" alt="image" src="https://github.com/user-attachments/assets/cc1972ab-c421-433f-bd7f-245c8b946b9f" />


---

## Architecture

```
climate-radar/
├── index.html              # Main application (self-contained, PIN-protected)
├── docs/
│   ├── ARCHITECTURE.md     # Technical design & component map
│   ├── SIGNAL_TAXONOMY.md  # How signals are classified and scored
│   ├── KEYWORD_GUIDE.md    # Keyword watch system documentation
│   └── USER_GUIDE.md       # End-user operational guide
├── data/
│   ├── signal_template.json    # Schema for adding new signals
│   └── keyword_watchlist.json  # Default keyword configuration
├── config/
│   └── radar_config.json       # Platform configuration settings
├── scripts/
│   ├── validate_links.py       # Automated source link validator
│   └── export_report.py        # Batch PDF export utility
├── assets/
│   └── README.md               # Asset management notes
├── CHANGELOG.md
├── CONTRIBUTING.md
└── .gitignore
```

---

## Features

| Feature | Description |
|---|---|
| Live Radar Display | Animated radar with blips representing active signals, color-coded by risk level |
| Threat Matrix | Real-time count of High / Medium / Low risk signals |
| Narrative Shift Index | Tracks directional changes in key climate language trends |
| Keyword Watch | User-defined keyword scanning across all signal sources |
| Link Verification | Automatic HEAD-check of every source URL on demand |
| PDF Export | One-click export of current filtered signals as a classified report |
| Live Scan | Fetches real-time signals from monitored climate sources with each scan run, updating the radar, signal feed, and counters with live data |
| Freshness Badges | NEW / RECENT / STALE indicators calculated from today's date |
| PIN Protection | SHA-256 hashed access code with session persistence |

---

## Access

The platform is PIN-protected. Access credentials are distributed to authorized team members only via secure channel.

To change the PIN: generate the SHA-256 hash of your new code and replace the `CORRECT_HASH` value in `index.html`.

```bash
# Generate a new PIN hash (example: new PIN is "9999")
python3 -c "import hashlib; print(hashlib.sha256('9999'.encode()).hexdigest())"
```

---

## Deployment

**Local:** Open `index.html` in any modern browser. No server required.

**GitHub Pages (private team):**
```bash
git clone https://github.com/NaifAlsalem/ClimateRadar
# Open index.html directly — or serve with:
python3 -m http.server 8080
```

**Requirements:** Chrome 90+, Firefox 88+, Edge 90+, Safari 14+

---

## Signal Sources

The platform currently monitors the following institutions:

- **IPCC:** Assessment reports and working group drafts
- **UNFCCC:** Negotiation texts, GST outcomes, COP agendas
- **IEA:** Energy outlook scenarios and demand projections
- **G7 / G20:** Communiqués and climate finance pledges
- **AU (African Union):** Coalition positions and declarations
- **UNEP / GMP:** Methane pledge progress and ministerial outcomes
- **EU Commission:** CBAM updates and regulatory expansions
- **Vision 2030:** Saudi sustainability alignment assessments

---

## Roadmap

- [ ] Live API integration (UNFCCC, IEA public feeds)
- [ ] Arabic language interface toggle
- [ ] Multi-user access with role levels
- [ ] Automated weekly digest PDF via cron
- [ ] Signal annotation and team notes
- [ ] Historical signal archive viewer

---

## Confidentiality

This repository is **private**. All contents are confidential and intended for authorized team use only. Redistribution is prohibited.

**© 2026 Dr. Naif Alsalem. All rights reserved.** 

