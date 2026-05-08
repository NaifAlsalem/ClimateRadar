# User Guide

## Getting Started

There are three ways to launch Climate Radar.

**Option 1 - Direct file open (simplest)**

Download `index.html` from the repository, double-click it, and it opens in your default browser. No setup required.

**Option 2 - From Git Bash**

```
cd ~/climate-radar
git pull origin main
start index.html
```

**Option 3 - From Command Prompt (Windows)**

```
cd C:\Users\YourName\climate-radar
git pull origin main
start index.html
```

If you do not have the repository on your machine yet, clone it first:

```
git clone https://github.com/NaifAlsalem/ClimateRadar.git
cd ClimateRadar
start index.html
```
Once the file opens, enter the access PIN at the authentication screen. The dashboard loads immediately after.

Chrome or Edge are recommended. The tool works on Firefox and Safari but has been tested most thoroughly on Chromium-based browsers.

---

## Interface Overview

### Left Column  (Intelligence Metrics)
- **Threat Matrix:** live count of High / Medium / Low risk signals
- **Narrative Shift Index:** directional trend bars for key climate language

### Center Column — Radar
- **Live radar display:** each blip represents an active signal
  - 🔴 Red blips = High risk (inner ring — closest to center)
  - 🟡 Yellow blips = Medium risk (middle ring)
  - 🟢 Green blips = Low risk (outer ring)
- **Signal counter:** This updates as you filter
- **Sources Scanned:** This increments with each new scan run
- **RUN NEW SCAN:** This re-sorts and refreshes the signal feed

### Right Column (Intelligence Feed)

#### Search Bar
Type any term to instantly filter signals across all tabs. Press ✕ to clear.

#### ALL TIME / RECENT Toggle
- **ALL TIME:** This shows all signals regardless of age
- **RECENT:** This filters to signals from the last 30 days only

#### Category Filters
Click any chip to filter by: Narrative | Policy | Negotiation | Finance | Alliance | Strategic

#### ⬇ PDF Button
Downloads a classified PDF report of all currently visible signals.

---

## Signal Cards

Each card shows:
- **Freshness badge:** shown as NEW / RECENT / age / STALE
- **Risk badge:** shown as HIGH / MEDIUM / LOW
- **Category**
- **Summary**
- **Source** and **date**

Click any card to open the **Signal Detail** panel on the right.

---

## Signal Detail Panel

Shows full signal information including:
- Risk classification
- Full summary
- Source, category, date
- **Link Verification:** This automatically checks if the source URL is reachable
  - ✓ LINK VERIFIED : domain is reachable
  - ✗ LINK UNREACHABLE : domain could not be reached
  -  TIMED OUT : no response within 7 seconds
  - RE-CHECK button to re-verify manually
- **VIEW SOURCE:** This opens the source page in a new tab
- **Section note:** This tells you exactly where in the document the signal appears

---

## Keyword Watch

Use the keyword bar to track specific terms across all signals:

1. Type a keyword in the input field and press **Enter** (or click **+ add keyword**)
2. Click **⌕ SCAN** to run the keyword search
3. Switch to the **KEYWORD RESULTS** tab to see matches
4. Matched keywords are highlighted on each card
5. Click ✕ next to any keyword to remove it

**Default keywords:** fossil fuel · CBAM · phase-out

**Suggested keywords to add:** carbon tax · net zero · oil demand · Arab Group · GCC · Article 6 · loss and damage

---

## PDF Export

The PDF report includes:
- Header with title and generation timestamp
- Active keyword watchlist
- Stats bar (total, High/Medium/Low counts)
- All currently filtered signals with full details and hyperlinks

> **Tip:** Apply filters before exporting as the PDF always reflects what is currently visible on screen.

---

## Access Code Management

The default access code is distributed separately. To change it:

1. Generate a SHA-256 hash of your new code:
   ```bash
   python3 -c "import hashlib; print(hashlib.sha256('NEWCODE'.encode()).hexdigest())"
   ```
2. Open `index.html` in a text editor
3. Find `const CORRECT_HASH = "..."` and replace with the new hash
4. Save and re-deploy

Never store the PIN in plain text anywhere in the repository.
