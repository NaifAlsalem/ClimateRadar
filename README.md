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
├── CHANGELOG.md                # Here we track every change in the repo
├── CONTRIBUTING.md             # Want to contribute? Please read through this and I would be very delighted to get you involved. 
└── .gitignore                  # Just a script to prevent unnecessary, sensitive, or system-generated files from being pushed to GitHub.
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

**First time setup - clone the repository:**

Launch PowerShell or Command Prompt from your computer and then write these commands in it:

```
git clone https://github.com/NaifAlsalem/ClimateRadar.git
cd ClimateRadar
start index.html
```
Example: 
<img width="392" height="223" alt="Screenshot 2026-05-10 085932" src="https://github.com/user-attachments/assets/5bac257f-27fc-4f23-8644-2e7c9158315d" />






**GitHub Pages (private team):**

# First time — clone the repository
git clone https://github.com/NaifAlsalem/ClimateRadar.git climate-radar

# Open the platform
cd climate-radar
start index.html

# To get the latest updates
git pull origin main
start index.html

# To start fresh — delete and reclone
cd ~
rm -rf climate-radar
git clone https://github.com/NaifAlsalem/ClimateRadar.git climate-radar




**Using Git Bash**


```
git clone https://github.com/NaifAlsalem/ClimateRadar
cd climateRadar
npx serve .
```
The local/network ID will be created and copied to to your clipboard. Go to the browser and paste it to get the platform launched. See the example below.
Example: 
<img width="651" height="440" alt="image" src="https://github.com/user-attachments/assets/d3aa87fe-ac13-47e5-be3e-03938dad6380" />



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

